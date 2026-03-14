import argparse
import json
from pathlib import Path


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Transcreve arquivos de audio em lote usando faster-whisper."
    )
    parser.add_argument(
        "inputs",
        nargs="+",
        help="Arquivos ou pastas para transcrever.",
    )
    parser.add_argument(
        "--glob",
        default="*.ogg",
        help="Padrao de busca quando a entrada for pasta. Ex.: *.ogg ou *.*",
    )
    parser.add_argument(
        "--model",
        default="small",
        help="Modelo do Whisper a usar. Ex.: tiny, base, small, medium.",
    )
    parser.add_argument(
        "--language",
        default="pt",
        help="Idioma esperado no audio. Ex.: pt, en, es.",
    )
    parser.add_argument(
        "--output-dir",
        default="transcricoes",
        help="Pasta onde os TXT e JSON serao salvos.",
    )
    return parser.parse_args()


def collect_files(inputs: list[str], pattern: str) -> list[Path]:
    files: list[Path] = []
    for raw in inputs:
        path = Path(raw)
        if path.is_file():
            files.append(path)
        elif path.is_dir():
            files.extend(sorted(path.glob(pattern)))
    seen: set[Path] = set()
    unique: list[Path] = []
    for item in files:
        resolved = item.resolve()
        if resolved not in seen:
            seen.add(resolved)
            unique.append(resolved)
    return unique


def ensure_engine():
    try:
        from faster_whisper import WhisperModel
    except ImportError as exc:
        raise SystemExit(
            "faster-whisper nao esta instalado. Rode: python -m pip install faster-whisper"
        ) from exc
    return WhisperModel


def write_outputs(output_dir: Path, audio_path: Path, text: str, segments: list[dict]) -> None:
    stem = audio_path.stem
    txt_path = output_dir / f"{stem}.txt"
    json_path = output_dir / f"{stem}.json"
    txt_path.write_text(text.strip() + "\n", encoding="utf-8")
    json_path.write_text(
        json.dumps(
            {
                "source": str(audio_path),
                "text": text.strip(),
                "segments": segments,
            },
            ensure_ascii=False,
            indent=2,
        ),
        encoding="utf-8",
    )


def main() -> None:
    args = parse_args()
    files = collect_files(args.inputs, args.glob)
    if not files:
        raise SystemExit("Nenhum arquivo encontrado para transcricao.")

    WhisperModel = ensure_engine()
    output_dir = Path(args.output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    model = WhisperModel(args.model, device="cpu", compute_type="int8")

    for audio_path in files:
        print(f"Transcrevendo: {audio_path}")
        segments_iter, info = model.transcribe(str(audio_path), language=args.language)
        segments = []
        parts = []
        for segment in segments_iter:
            segments.append(
                {
                    "start": segment.start,
                    "end": segment.end,
                    "text": segment.text.strip(),
                }
            )
            parts.append(segment.text.strip())
        text = " ".join(part for part in parts if part).strip()
        write_outputs(output_dir, audio_path, text, segments)
        print(
            f"Concluido: {audio_path.name} | idioma={info.language} | prob={info.language_probability:.2f}"
        )


if __name__ == "__main__":
    main()

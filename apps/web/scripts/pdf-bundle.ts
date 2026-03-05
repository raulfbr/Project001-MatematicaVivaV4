import { join } from "node:path";

import { loadAllLessons } from "../lib/content/loader";
import { readLessonArtifact, renderPdfFromArtifacts } from "./pdf-common";

function parseRangeArg(flag: "--from" | "--to"): string {
  const idx = process.argv.indexOf(flag);
  if (idx >= 0 && process.argv[idx + 1]) return process.argv[idx + 1];
  throw new Error(`Missing ${flag} MV-S-XXX`);
}

async function main() {
  const from = parseRangeArg("--from");
  const to = parseRangeArg("--to");

  const lessons = await loadAllLessons();
  const ordered = lessons.sort((a, b) => a.meta.order - b.meta.order);
  const fromOrder = ordered.find((l) => l.meta.id === from)?.meta.order;
  const toOrder = ordered.find((l) => l.meta.id === to)?.meta.order;

  if (fromOrder === undefined || toOrder === undefined) {
    throw new Error("Invalid range IDs");
  }

  const min = Math.min(fromOrder, toOrder);
  const max = Math.max(fromOrder, toOrder);

  const ids = ordered.filter((l) => l.meta.order >= min && l.meta.order <= max).map((l) => l.meta.id);
  const artifacts = await Promise.all(ids.map(readLessonArtifact));

  const out = join(process.cwd(), "..", "..", "dist", "pdf", `bundle-${from}-${to}.pdf`);

  await renderPdfFromArtifacts({
    title: `Caderno ${from} ate ${to}`,
    artifacts,
    outputPdfPath: out,
    reportLabel: "bundle"
  });

  console.log(`PDF bundle generated: ${out}`);
}

main().catch((err) => {
  console.error(err.message ?? err);
  process.exit(1);
});

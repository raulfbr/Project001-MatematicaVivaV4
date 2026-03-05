import { join } from "node:path";

import { readLessonArtifact, renderPdfFromArtifacts } from "./pdf-common";

function parseLessonId(): string {
  const idx = process.argv.indexOf("--id");
  if (idx >= 0 && process.argv[idx + 1]) return process.argv[idx + 1];
  throw new Error("Missing --id MV-S-XXX");
}

async function main() {
  const lessonId = parseLessonId();
  const artifact = await readLessonArtifact(lessonId);
  const out = join(process.cwd(), "..", "..", "dist", "pdf", `${lessonId}.pdf`);

  await renderPdfFromArtifacts({
    title: `Licao ${lessonId}`,
    artifacts: [artifact],
    outputPdfPath: out,
    reportLabel: "single"
  });

  console.log(`PDF single generated: ${out}`);
}

main().catch((err) => {
  console.error(err.message ?? err);
  process.exit(1);
});

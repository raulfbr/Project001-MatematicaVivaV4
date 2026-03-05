import { join } from "node:path";

import { loadAllLessons } from "../lib/content/loader";
import { readLessonArtifact, renderPdfFromArtifacts } from "./pdf-common";

async function main() {
  const lessons = await loadAllLessons();
  const orderedIds = lessons.sort((a, b) => a.meta.order - b.meta.order).map((l) => l.meta.id);
  const artifacts = await Promise.all(orderedIds.map(readLessonArtifact));

  const out = join(process.cwd(), "..", "..", "dist", "pdf", "caderno-sementes-full.pdf");

  await renderPdfFromArtifacts({
    title: "Caderno Sementes Completo",
    artifacts,
    outputPdfPath: out,
    reportLabel: "full-sementes"
  });

  console.log(`PDF full generated: ${out}`);
}

main().catch((err) => {
  console.error(err.message ?? err);
  process.exit(1);
});

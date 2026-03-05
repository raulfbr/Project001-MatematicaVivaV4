import { readdir } from "node:fs/promises";
import { join } from "node:path";

import { loadLessonById } from "../lib/content/loader";
import { resolveLesson } from "../lib/content/resolver";
import { runLessonGates } from "../lib/qa/gates";

type Mode = "preview" | "publish";

function parseMode(): Mode {
  const modeIndex = process.argv.indexOf("--mode");
  if (modeIndex >= 0) {
    const value = process.argv[modeIndex + 1];
    if (value === "preview" || value === "publish") return value;
  }
  return "preview";
}

async function main() {
  const mode = parseMode();
  const lessonsRoot = join(process.cwd(), "..", "..", "content", "lessons");
  const entries = await readdir(lessonsRoot, { withFileTypes: true });
  const lessonIds = entries.filter((e) => e.isDirectory()).map((e) => e.name).sort();

  const errors: string[] = [];
  const warnings: string[] = [];

  for (const lessonId of lessonIds) {
    const lesson = await loadLessonById(lessonId);
    const resolved = resolveLesson(lesson);
    const gate = runLessonGates(resolved, mode);

    gate.errors.forEach((e) => errors.push(`${lessonId}: ${e}`));
    gate.warnings.forEach((w) => warnings.push(`${lessonId}: ${w}`));
  }

  if (warnings.length > 0) {
    console.warn(`Warnings (${warnings.length}):`);
    warnings.forEach((w) => console.warn(` - ${w}`));
  }

  if (errors.length > 0) {
    console.error(`Errors (${errors.length}):`);
    errors.forEach((e) => console.error(` - ${e}`));
    process.exit(1);
  }

  console.log(`Lessons validation OK in ${mode} mode. Lessons: ${lessonIds.length}`);
}

main().catch((err) => {
  console.error(err);
  process.exit(1);
});

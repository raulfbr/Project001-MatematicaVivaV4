import { mkdir, writeFile } from "node:fs/promises";
import { join } from "node:path";

import { loadAllLessons } from "../lib/content/loader";
import { attachNavigation, resolveLesson } from "../lib/content/resolver";
import { runLessonGates } from "../lib/qa/gates";
import { scoreFromGate } from "../lib/qa/score";

async function main() {
  const lessons = await loadAllLessons();
  const resolvedWithNav = attachNavigation(lessons.map(resolveLesson));

  const lessonReports = resolvedWithNav.map((lesson) => {
    const gate = runLessonGates(lesson, "preview");
    const score = scoreFromGate(gate);
    return {
      id: lesson.id,
      slug: lesson.slug,
      title: lesson.title,
      variant: lesson.variant,
      gateStatus: gate.gateStatus,
      errors: gate.errors,
      warnings: gate.warnings,
      scoreTotal: score.total,
      scoreByAxis: score.byAxis,
      navigation: lesson.navigation
    };
  });

  const avg = lessonReports.reduce((acc, l) => acc + l.scoreTotal, 0) / lessonReports.length;

  const report = {
    batch: "pilot",
    generatedAt: new Date().toISOString(),
    summary: {
      lessons: lessonReports.length,
      avgScore: Number(avg.toFixed(2)),
      blockingErrors: lessonReports.flatMap((l) => l.errors).length
    },
    lessons: lessonReports,
    blockingErrors: lessonReports.flatMap((l) => l.errors)
  };

  const outDir = join(process.cwd(), "..", "..", "dist", "reports");
  await mkdir(outDir, { recursive: true });
  await writeFile(join(outDir, "quality_report.json"), JSON.stringify(report, null, 2), "utf8");

  console.log(`quality_report.json generated: ${report.summary.lessons} lessons, avg ${report.summary.avgScore}`);
}

main().catch((err) => {
  console.error(err);
  process.exit(1);
});

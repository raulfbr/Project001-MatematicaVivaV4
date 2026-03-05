import { mkdir, writeFile } from "node:fs/promises";
import { join } from "node:path";

import { loadAllLessons } from "../lib/content/loader";
import { attachNavigation, resolveLesson } from "../lib/content/resolver";
import { runLessonGates } from "../lib/qa/gates";
import { scoreFromGate } from "../lib/qa/score";

async function main() {
  const lessons = await loadAllLessons();
  const resolved = attachNavigation(lessons.map(resolveLesson));

  const artifactsDir = join(process.cwd(), "..", "..", "dist", "artifacts", "lessons");
  const reportsDir = join(process.cwd(), "..", "..", "dist", "reports");
  const navDir = join(process.cwd(), "..", "..", "dist", "artifacts", "navigation");

  await mkdir(artifactsDir, { recursive: true });
  await mkdir(reportsDir, { recursive: true });
  await mkdir(navDir, { recursive: true });

  const pendingEntries: Array<{
    lessonId: string;
    blockId: string;
    severity: "warning" | "error";
    reason: string;
  }> = [];

  const variantCount: Record<string, number> = {};

  for (const lesson of resolved) {
    const gate = runLessonGates(lesson, "preview");
    const score = scoreFromGate(gate);

    lesson.missingRequiredBlocks.forEach((blockId) => {
      pendingEntries.push({
        lessonId: lesson.id,
        blockId,
        severity: "warning",
        reason: "Missing required block content in preview"
      });
    });

    variantCount[lesson.variant] = (variantCount[lesson.variant] ?? 0) + 1;

    const artifact = {
      meta: {
        id: lesson.id,
        slug: lesson.slug,
        title: lesson.title,
        order: lesson.order,
        cycle: "Sementes"
      },
      variant: lesson.variant,
      blocks: lesson.blocks,
      navigation: lesson.navigation,
      quality: {
        score: score.total,
        gateStatus: gate.gateStatus,
        errors: gate.errors,
        warnings: gate.warnings
      },
      build: {
        mode: "preview",
        timestamp: new Date().toISOString(),
        commit: process.env.GIT_COMMIT_SHA ?? "local"
      }
    };

    await writeFile(join(artifactsDir, `${lesson.id}.json`), JSON.stringify(artifact, null, 2), "utf8");
  }

  const pendingReport = {
    generatedAt: new Date().toISOString(),
    totalPending: pendingEntries.length,
    entries: pendingEntries
  };

  const variantReport = {
    generatedAt: new Date().toISOString(),
    totalLessons: resolved.length,
    byVariant: variantCount,
    lessons: resolved.map((l) => ({ id: l.id, slug: l.slug, variant: l.variant }))
  };

  const navigationIndex = {
    generatedAt: new Date().toISOString(),
    lessons: resolved.map((l) => ({ id: l.id, slug: l.slug, navigation: l.navigation }))
  };

  await writeFile(join(reportsDir, "pending_report.json"), JSON.stringify(pendingReport, null, 2), "utf8");
  await writeFile(join(reportsDir, "variant_report.json"), JSON.stringify(variantReport, null, 2), "utf8");
  await writeFile(join(navDir, "index.json"), JSON.stringify(navigationIndex, null, 2), "utf8");

  console.log(`Artifacts generated: ${resolved.length} lessons`);
  console.log(`pending_report.json entries: ${pendingEntries.length}`);
  console.log(`variant_report.json variants: ${Object.keys(variantCount).join(", ")}`);
}

main().catch((err) => {
  console.error(err);
  process.exit(1);
});

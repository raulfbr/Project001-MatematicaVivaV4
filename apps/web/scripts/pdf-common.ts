import { mkdir, readFile, writeFile } from "node:fs/promises";
import { join } from "node:path";

import { chromium } from "playwright";

export interface LessonArtifact {
  meta: {
    id: string;
    slug: string;
    title: string;
  };
  variant: string;
  blocks: Array<{ id: string; label: string; content: unknown }>;
}

export async function readLessonArtifact(lessonId: string): Promise<LessonArtifact> {
  const path = join(process.cwd(), "..", "..", "dist", "artifacts", "lessons", `${lessonId}.json`);
  const raw = await readFile(path, "utf8");
  return JSON.parse(raw) as LessonArtifact;
}

function htmlEscape(text: string): string {
  return text
    .replaceAll("&", "&amp;")
    .replaceAll("<", "&lt;")
    .replaceAll(">", "&gt;")
    .replaceAll('"', "&quot;");
}

function stringifyContent(content: unknown): string {
  if (content === null || content === undefined) return "";
  if (typeof content === "string") return content;
  return JSON.stringify(content, null, 2);
}

export function renderArtifactHtml(title: string, artifacts: LessonArtifact[]): string {
  const sections = artifacts
    .map((artifact) => {
      const blocks = artifact.blocks
        .map((b) => {
          const text = htmlEscape(stringifyContent(b.content));
          return `<section class=\"block\"><h3>${htmlEscape(b.label)}</h3><pre>${text}</pre></section>`;
        })
        .join("\n");

      return `<article class=\"lesson\"><h2>${htmlEscape(artifact.meta.id)} - ${htmlEscape(artifact.meta.title)}</h2>${blocks}</article>`;
    })
    .join("\n<hr/>\n");

  return `<!doctype html>
<html lang="pt-BR">
<head>
<meta charset="utf-8" />
<title>${htmlEscape(title)}</title>
<style>
  body { font-family: Arial, sans-serif; color: #1f2937; margin: 0; padding: 20px; }
  h1 { margin: 0 0 16px; }
  h2 { margin-top: 18px; font-size: 18px; }
  h3 { margin: 10px 0 6px; font-size: 13px; text-transform: uppercase; letter-spacing: .05em; color: #6b7280; }
  pre { white-space: pre-wrap; font-size: 12px; background: #f9fafb; border: 1px solid #e5e7eb; padding: 10px; border-radius: 8px; }
  .block { break-inside: avoid; margin-bottom: 10px; }
  .lesson { break-after: page; }
  .lesson:last-child { break-after: auto; }
  @page { size: A4; margin: 14mm; }
</style>
</head>
<body>
<h1>${htmlEscape(title)}</h1>
${sections}
</body>
</html>`;
}

export async function renderPdfFromArtifacts(opts: {
  title: string;
  artifacts: LessonArtifact[];
  outputPdfPath: string;
  reportLabel: string;
}) {
  await mkdir(join(process.cwd(), "..", "..", "dist", "pdf"), { recursive: true });
  await mkdir(join(process.cwd(), "..", "..", "dist", "reports"), { recursive: true });

  const browser = await chromium.launch();
  const page = await browser.newPage();

  const html = renderArtifactHtml(opts.title, opts.artifacts);
  await page.setContent(html, { waitUntil: "domcontentloaded" });

  await page.pdf({
    path: opts.outputPdfPath,
    format: "A4",
    printBackground: true,
    margin: { top: "14mm", right: "14mm", bottom: "14mm", left: "14mm" }
  });

  await browser.close();

  const reportPath = join(process.cwd(), "..", "..", "dist", "reports", "pdf_report.json");
  let report = {
    generatedAt: new Date().toISOString(),
    entries: [] as Array<{ label: string; output: string; lessons: string[]; status: "ok" | "fail" }>
  };

  try {
    const prev = await readFile(reportPath, "utf8");
    report = JSON.parse(prev) as typeof report;
  } catch {
    // no previous report
  }

  report.generatedAt = new Date().toISOString();
  report.entries.push({
    label: opts.reportLabel,
    output: opts.outputPdfPath,
    lessons: opts.artifacts.map((a) => a.meta.id),
    status: "ok"
  });

  await writeFile(reportPath, JSON.stringify(report, null, 2), "utf8");
}

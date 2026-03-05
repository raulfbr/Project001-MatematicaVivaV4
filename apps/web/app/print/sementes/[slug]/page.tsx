import { notFound } from "next/navigation";

import { BlockRenderer } from "@/components/lesson/block-renderer";
import { loadAllLessons } from "@/lib/content/loader";
import { attachNavigation, resolveLesson } from "@/lib/content/resolver";

export default async function LessonPrintPage({ params }: { params: Promise<{ slug: string }> }) {
  const { slug } = await params;
  const lessons = await loadAllLessons();
  const resolvedLessons = attachNavigation(lessons.map(resolveLesson));
  const resolved = resolvedLessons.find((l) => l.slug === slug);

  if (!resolved) return notFound();

  return (
    <main className="container">
      <p className="block-label">Modo Impressao A4</p>
      <BlockRenderer lesson={resolved} />
    </main>
  );
}

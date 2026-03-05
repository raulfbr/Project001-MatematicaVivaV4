import Link from "next/link";
import type { ResolvedLesson } from "@/lib/content/resolver";

function renderValue(value: unknown): string {
  if (value === null || value === undefined) return "";
  if (typeof value === "string") return value;
  return JSON.stringify(value, null, 2);
}

export function BlockRenderer({ lesson }: { lesson: ResolvedLesson }) {
  return (
    <section>
      <h1>{lesson.title}</h1>
      <p>Variant: {lesson.variant}</p>
      <nav>
        {lesson.navigation.prev ? <Link href={`/sementes/${lesson.navigation.prev.slug}`}>← {lesson.navigation.prev.title}</Link> : null}{" "}
        {lesson.navigation.next ? <Link href={`/sementes/${lesson.navigation.next.slug}`}>{lesson.navigation.next.title} →</Link> : null}
      </nav>
      {lesson.blocks.map((block) => (
        <article key={block.id} className="lesson-block">
          <div className="block-label">{block.label}</div>
          <pre>{renderValue(block.content)}</pre>
        </article>
      ))}
    </section>
  );
}

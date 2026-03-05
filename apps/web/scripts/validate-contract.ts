import { LESSON_STRUCTURE_CONTRACT } from "../lib/contracts/lesson-structure";

const blockIds = new Set<string>();
for (const block of LESSON_STRUCTURE_CONTRACT.blocks) {
  if (blockIds.has(block.id)) {
    console.error(`Duplicate block id: ${block.id}`);
    process.exit(1);
  }
  blockIds.add(block.id);
}

if (LESSON_STRUCTURE_CONTRACT.blocks.length === 0) {
  console.error("Contract has no blocks.");
  process.exit(1);
}

console.log(`Contract OK: ${LESSON_STRUCTURE_CONTRACT.blocks.length} blocks, version ${LESSON_STRUCTURE_CONTRACT.contractVersion}`);

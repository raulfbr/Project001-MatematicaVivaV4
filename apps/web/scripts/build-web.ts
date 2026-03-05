import { spawnSync } from "node:child_process";

const cwd = process.cwd();
if (cwd.includes("!")) {
  console.error("Build blocked: current path contains '!'.");
  console.error(`Path: ${cwd}`);
  console.error("Webpack/Next rejects '!' in absolute paths (loader syntax conflict).");
  console.error("Action: run this project from a path without '!' to execute next build.");
  process.exit(1);
}

const nextBin = require.resolve("next/dist/bin/next");
const result = spawnSync(process.execPath, [nextBin, "build"], {
  stdio: "inherit",
  cwd
});

if (result.status !== 0) process.exit(result.status ?? 1);

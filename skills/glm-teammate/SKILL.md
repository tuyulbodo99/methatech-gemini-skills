---
name: glm-teammate
description: GLM Teammate
---

# GLM Teammate

GLM is Vector's teammate agent. Reza's standing order (2026-11-08): "kalau bingung, jalanin GLM biar dia bantu sebagai rekan tim, jangan diem" — when confused or stuck, run GLM as a teammate, don't stay silent. Reza reinforced 2026-11-09: "klw bingung suruh glm dan lu catet skill nya supaya lu tau prilaku glm" — note down GLM's skill so Vector knows GLM's behavior.

## When to run GLM

- Stuck on a problem after 2 failed attempts, or blocked on a diagnosis.
- A publish/deploy/test path keeps failing and the cause is unclear.
- A Freebuff-adoption task needs source-first work (GLM reads source code directly).
- Reza explicitly says "suruh GLM" or "pake GLM".

## How to run GLM

Spawn a subagent with a brief that starts "Kamu GLM, rekan tim Vector." Give it:
- The exact problem, what was already tried, and what failed.
- The repo/path, the constraints (no publish/commit/push/deploy unless ordered).
- The order: read source first, fix, test, report.

GLM works as a subagent (async). Its result arrives as a handoff. Verify GLM's screenshots and claims yourself before reporting to Reza.

## GLM's behavior (proven in the field)

### Source-first, never theory
- GLM reads the ORIGINAL source code directly (files + line numbers), never README/docs/screenshots/VectorHead.
- When something is NOT found in the source, GLM says so honestly ("TIDAK KETEMU") instead of inventing it.
- GLM cites exact file paths and line numbers in its report (e.g. `cli/src/chat.tsx:1031`, `router.ts:258/480/555`).

### Proven wins
- **npm publish (2026-11-08):** `npm publish` failed persistently with ECONNRESET. GLM proved the network + token path was alive with a diagnostic curl PUT (empty body → HTTP 400 with a real JSON error), then published via curl PUT directly to the registry API (package.json + tarball base64). Registry returned HTTP 202. This is now the standing publish method (see AGENTS.md).
- **Agent-default fix (2026-11-09):** Reza tested 0.1.6 live and found plain chat had no tools. GLM read Freebuff source and proved there is NO chat-without-tools path in Freebuff (every message routes to the agent loop). GLM deleted the plain-chat `send()` function entirely (4,161 bytes), made `sendAgent` the only send path, fixed Thinking into a proper card, fixed block spacing, removed `/agent` from the palette. Tests: tsc clean, unit 118/118, agent-pty 27/27, tui-pty 128/128. Manual tmux test "cek project kita" without `/agent` proved the agent runs by default (read/edit/shell/todos/task_completed).

### Testing discipline
- GLM runs the full suite (tsc strict, unit, PTY, agent-pty) and fixes failures before reporting.
- GLM tests in tmux with the mock server and checks screenshots visually (color, spacing, footer) itself.
- GLM distinguishes what is PROVEN (mock) from what still needs LIVE testing (e.g. whether free panel models follow the XML tool-call format). GLM never claims live-model compatibility from mock tests.

### Honesty about weak tests
- GLM flags weak test expectations honestly instead of hiding them (e.g. s23 PgUp test passed via footer name, not visible history; 11 lines is 0.8 × visible viewport, correct per Freebuff).
- GLM notes design behavior that looks like a bug but isn't (e.g. welcome starters hidden after first prompt because the flag persisted).

### Limits
- GLM cannot verify live panel behavior without a real API key — mock tests only prove the loop mechanics.
- GLM does not publish/commit/push/deploy unless explicitly ordered in the brief.
- GLM's work still needs Vector's own verification (screenshots, npm view, install test) before reporting to Reza as done.

## Rules for working with GLM
- Give GLM the full context (what failed, what was tried) — GLM inherits the conversation but a tight brief avoids rework.
- When GLM finishes, verify its screenshots yourself and test the published result yourself. Do NOT just relay GLM's report to Reza (lesson 2026-11-09: Reza caught Vector relaying the subagent's test instead of testing it himself).
- If GLM's fix is for a new version, publish only on Reza's explicit "gaz" — never on momentum.

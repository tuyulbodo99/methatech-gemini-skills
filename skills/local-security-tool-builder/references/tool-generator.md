# Mode 4 — Tool Generator

When the user asks for a tool ("buatkan tool untuk X"):

1. **Understand** the goal; define input/output explicitly.
2. **Check** what already exists (installed binaries, prior workspace tools) — don't rebuild.
3. **Choose** the simplest language (Python default).
4. **Scaffold** the project layout (see SKILL.md Operating Rules).
5. **Implement** with error handling + logging from the start.
6. **Test**: input validation, happy path, invalid input, network timeout, empty response, malformed response, permission error, file error.
7. **Fix** failures via the debug playbook in [environment.md](environment.md).
8. **Document**: README with usage command, e.g. `tool --target http://localhost:8080 --output report.json`.
9. **Final report** per SKILL.md format.

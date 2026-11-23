---
name: local-security-tool-builder
description: Local security tool builder
---

# Local security tool builder

## Choose the mode and read its reference

- Pick the mode that fits the request before you build anything.

- Choose between the web scraper builder, the security testing mode, the APK analysis mode and the generic tool generator mode by the request wording.

- Read the matching reference with `muse.read` and follow its full contract before you write code.

- Search the Sectinel playbook library with the helper at `~/workspace/custom-skills/local-security-tool-builder/bin/search-arsenal.py` when the task matches a playbook domain, then read the matched SKILL.md and follow it.

- Do not run the Sectinel installer in this environment because its targets are different product paths and the checkout itself is the library.

## Establish the boundary before running

- State TARGET AUTHORIZATION ENVIRONMENT SCOPE ACTION before you run any security tooling.

- Run active tests only on localhost, 127.0.0.1, a private lab, a CTF, an emulator, the user own device or server, or a target with explicit written permission.

- Stop at passive analysis or build a local simulation when authorization is unclear.

- Never access systems, accounts, networks or data without permission and never harvest credentials, tokens, cookies, API keys or personal data.

- Never use credential stuffing, phishing, malware persistence, privilege escalation against real targets or auth bypass.

- Prefer official APIs for scraping and respect robots.txt, terms of service and rate limits with conservative rate limiting.

- Never defeat CAPTCHA, login walls or access controls.

- Analyze only the user own APK or one the user explicitly permits and never steal credentials, session tokens, keys or user data from third party apps.

- Put secrets in environment variables and never hardcode them in source.

## Build test and debug

- Check what already exists before you build and reuse installed binaries such as curl, adb, apktool and jadx when they fit.

- Use a virtualenv or user space installs and never destructively change system config.

- Default to the simplest language that fits and use Python first for scrapers and analyzers.

- Use this project layout with README.md, requirements.txt, config.example.json, src, tests and output.

- Run the environment audit and test matrix in references/environment.md before you build.

- Test each case and on failure report ERROR, CAUSE, FIX and TEST RESULT instead of a bare failure message.

- Never delete data without confirmation and keep correct exit codes, error handling and logging in every tool.

## Report the result

- End every build with STATUS SUCCESS, PARTIAL or FAILED.

- Report the tool name and version, the environment with key tool versions, the files created, the cases tested and the outcome per case.

- Report known limitations, the usage command and the next recommended step.

## Available connectors

- Use `muse.connector_search` to find other connectors and `muse.skill_search` to find related skills.

- If nothing here fits, look on the web for a maintained API or MCP server and set it up with [Custom Connectors and MCPs](/opt/muse/skills/custom-connector-setup/SKILL.md), or build a custom connector.

## Alternatives for better results

- Build a local simulation of the target first when real target access is not yet confirmed so you can test the tool safely.

- Reuse an installed binary or an existing helper before you write new code so the tool stays small and reproducible.

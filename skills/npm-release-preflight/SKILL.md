---
name: npm-release-preflight
description: npm Release Preflight
---

# npm Release Preflight

## Check the version is free

- Read the version in `package.json` and run `npm view <package>` to see the latest published version before you change anything else.

- Bump the version when the version in `package.json` is already published, because publishing the same version again fails and wastes the audit.

- Wait out the registry read lag of a few minutes before you treat a fresh publish as missing, and never publish the same version twice.

- Confirm the git tag for the new version does not already point at another commit, and move on only when the version and the tag are both free.

## Match the changelog lockfile and README

- Add a CHANGELOG section for the new version that names the work in this release and the test counts from the tree you will publish.

- Read the test counts from a fresh test run on that tree, and do not copy counts from an older audit or an older release.

- Open `package-lock.json` and confirm its version matches `package.json`, and regenerate the lockfile when the two disagree.

- Search the README for the old version number and update every reference to the new version, including any line that points at the changelog for the new release.

- List the tracked modified files and the untracked files in the tree, and confirm every file the release needs is present and no stale file is included.

## Rebuild clean and inspect the pack

- Run `rm -rf dist` and then `npm run build`, because the compiler does not remove a compiled file whose source was deleted.

- Run `npm test` on the rebuilt tree and record the unit test count and the PTY test counts before you pack.

- Run `npm pack --dry-run` and read the file count and the file list, then confirm the version is the new one and the list holds no test files, docs, source files, backups or stale compiled files.

- Record the pack shasum with the file count, so the audit can compare the exact pack you checked against the pack you publish.

- Publish only after every check above passes, and use the curl PUT publish route when the npm client keeps failing with a reset connection.

## Report the preflight result

- Report the version, the changelog section, the lockfile match, the README grep result, the pack file count and shasum, and the test counts in one short list.

- Name any check that failed and the fix you applied, and rerun the affected checks after the fix instead of assuming the fix worked.

- Verify the published install with a fresh install and the version command, and report the installed version before you call the release done.

## Available connectors

- Use `muse.connector_search` to find other connectors and `muse.skill_search` to find related skills.

- If nothing here fits, look on the web for a maintained API or MCP server and set it up with [Custom Connectors and MCPs](/opt/muse/skills/custom-connector-setup/SKILL.md), or build a custom connector.

## Alternatives for better results

- Run this preflight before the release audit, not during it, so the audit judges the release instead of catching mechanical items.

- Keep the publish step separate from the preflight, and let the release audit stay the final gate after preflight passes.

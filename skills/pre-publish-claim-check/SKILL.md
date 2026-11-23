---
name: pre-publish-claim-check
description: Verify factual claims before publishing
---

# Verify factual claims before publishing

## Extract each factual claim

- Read the full draft and list every factual claim on its own line.

- Treat a price, a quota, a free tier limit, an availability date, a region restriction, a feature list, and a plan tier as a factual claim.

- Treat a paraphrase as a claim when a reader could rely on it as a fact.

- Keep the exact wording of each claim beside it so the check tests what will actually publish.

## Check each claim against an official source

- Find the official pricing page, documentation page, announcement, or changelog for each claim.

- Open the official source fresh for this draft and do not rely on memory of an earlier version.

- Record the source URL and the date you checked it beside each claim.

- Mark a claim as verified only when the official source states the same fact in the same scope.

- Mark a claim as unverified when the official source is blocked, missing, silent, or states a different scope.

## Check standing wording bans before approval

- Read the standing caption wording bans from memory before you check the draft, and treat each ban as a hard rule for this draft.

- Scan the exact caption text for banned honesty words and phrases, including jujur and catatan jujur and any self referential honesty disclaimer, in any casing and in any position.

- Remove each banned phrase you find and rewrite the sentence to state the fact directly without comment on honesty.

- Treat a banned phrase found after approval as a changed caption, and seek fresh approval for the rewritten caption before you publish it.

## Handle unverified or changed claims

- Rewrite an unverified claim to match only what the official source states.

- Remove a claim when no official source supports it and no narrower true version remains.

- Add an availability note when a feature applies only to one plan, region, or rollout group.

- Add an effective date when a fact changed over time, such as a restriction that was later lifted.

- Do not publish an unverified claim while waiting for a user verdict.

## Present verification with the draft

- Show the user the claim list with one status per claim and one source link per verified claim.

- Name each changed or removed claim and say what the official source states instead.

- List any banned wording you removed beside the claim list, so the user sees what changed and why.

- Ask the user to choose leave, add a clarification, or correct when an already published item carries a wrong claim.

- Never edit a live published post silently to fix a claim.

## Available connectors

- Use `muse.connector_search` to find other connectors and `muse.skill_search` to find related skills.

- If nothing here fits, look on the web for a maintained API or MCP server and set it up with [Custom Connectors and MCPs](/opt/muse/skills/custom-connector-setup/SKILL.md), or build a custom connector.

## Alternatives for better results

- Check the claim at the source the provider controls rather than a summary, a screenshot of a summary, or a secondhand post.

- Recheck a claim when the draft was written days earlier because pricing, limits, and rollout status change without notice.

- Keep one short claim list per draft so a later correction can trace each fact to its source.

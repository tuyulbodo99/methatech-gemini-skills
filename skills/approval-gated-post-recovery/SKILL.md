---
name: approval-gated-post-recovery
description: Approval Gated Post Recovery
---

# Approval Gated Post Recovery

## Name the exact approval card

- Name the slot time, the destination, and the scheduled time in the user timezone every time you ask about an approval card.

- Never ask the user to approve the card without those three identifiers, because a bare approval request cannot be matched to one post.

- List each pending approval separately when two jobs need approval in the same hour, and ask which one the user acted on.

- Never treat approval of one job as approval of another job, even when the jobs ran in the same hour.

- Tell the user where the approval card appears when they are on a channel that cannot show it, and direct them to that place to act on it.

## Check the destination before you nudge

- Read the destination timeline before any nudge or retry, and stop when the post is already live.

- Report a live post with its time and destination, and do not create a second post for the same slot.

- Treat a scheduled job that reports unfinished work as stalled rather than published, and check the timeline again before acting.

- Do not post manually from a background worker for a slot handled by a scheduled job, because the original command can still run after approval and create a duplicate.

## Recover only after expiry is confirmed

- Confirm whether the approval card is still pending before recreating anything, and let the original command run while the card is still pending.

- Recreate the post only when the card is gone or expired and the post is still absent from the timeline.

- Recreate the post from the main chat rather than from a background worker, so the new approval card appears where the user can act on it.

- Recreate the post with the exact approved text and destination, and seek fresh approval for any change to the text, media, audience, or destination.

- Verify the recreated post on the timeline after approval, and report each destination separately as live, scheduled, or still failed with its reason.

## Available connectors

- [Facebook](/opt/hatch/connectors/facebook_cli/CONNECTOR.md) for personal text posts and for reading the personal timeline to verify a post.

- Use `muse.connector_search` to find other connectors and `muse.skill_search` to find related skills.

- If nothing here fits, look on the web for a maintained API or MCP server and set it up with [Custom Connectors and MCPs](/opt/muse/skills/custom-connector-setup/SKILL.md), or build a custom connector.

## Alternatives for better results

- Ask the user to act on one approval card at a time when two jobs need approval in the same hour, so each approval maps to exactly one post.

- Surface the approval card in the main chat at once rather than reasking what the user meant, so a stalled slot is named and checked in the same turn.

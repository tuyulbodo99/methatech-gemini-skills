---
name: github-repo-content-pack
description: GitHub Repo Content Pack
---

# GitHub Repo Content Pack

## Vet the repo from the live page

- Open the repo's github.com page with `browser.browse` and read the current stars, forks, license, last commit date and the one line description of what it does.

- Take every number from the live page, never from memory. Carry the exact repo URL into the browser task and verify each fact there.

- Skip repos with no license, no commits in the last year, or single digit stars unless the user asked for that niche. State plainly why a repo did not make the cut.

## Capture the README-only dark mobile screenshot

- Capture only the README section in dark mode, cropped to a mobile portrait frame. Generate nothing with AI for this image.

- Open the PNG after capture and confirm it shows the official repo page with readable text. Re-shoot a failed capture instead of shipping it.

## Write the caption and the link

- Write a short casual caption in Bahasa Indonesia: what the repo does in one line, its star count, and the official github.com link at the end.

- Check every factual claim in the caption with the [Pre-publish Claim Check](~/workspace/custom-skills/pre_publish_claim_check/SKILL.md) method before delivery.

- Keep the caption copy-paste ready so the user can post it as-is.

## Deliver for the destination

- Send text to the personal profile through the Facebook connector, which accepts no image slot. Hand the screenshot and video to the user as files for manual upload.

- Draft or schedule Page posts with the media attached, following [Social Publishing](/opt/muse/skills/social-publishing/SKILL.md) for approval and verification.

- Offer an optional 9:16 vertical video assembled from the screenshot with ffmpeg or Concat. Say plainly that this is camera motion over a still image, not AI generated video.

## Available connectors

- [Facebook](/opt/hatch/connectors/facebook_cli/CONNECTOR.md) for personal text posts and Page drafts, posts and scheduling.

- Use `muse.connector_search` to find other connectors and `muse.skill_search` to find related skills.

- If nothing here fits, look on the web for a maintained API or MCP server and set it up with [Custom Connectors and MCPs](/opt/muse/skills/custom-connector-setup/SKILL.md), or build a custom connector.

## Websites

- [GitHub](https://github.com/) for vetting repos and capturing README screenshots. Carry the exact repo URL into `browser.browse` and verify stars, forks, license and last update there.

## Alternatives for better results

- Batch several repos in one research pass and deliver the strongest first, so one weak repo does not waste a post slot.

- Capture the repo header plus the top of the README when the full README is too long for one frame, and let the caption carry the detail.

- Fall back to light mode when dark mode renders code blocks unreadably, and keep the mobile portrait crop.

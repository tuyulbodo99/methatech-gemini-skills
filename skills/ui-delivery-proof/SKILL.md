---
name: ui-delivery-proof
description: Prove a UI fix before sending it
---

# Prove a UI fix before sending it

## Measure the exact element

- Measure the changed element in pixels before you change it, including its spacing, its alignment, its gap to neighbouring elements, and whether a separating line is present.

- Measure the same properties again after the change and compare the two sets of numbers instead of judging the result by eye.

- List every property the user named in the correction, and check each one separately, so one fixed property does not hide another broken property.

- After a user corrects the same element once, stop sending new guesses and remeasure all of its related properties before the next delivery.

## Capture proof the user can trust

- Capture an ordinary viewport screenshot at the width the user will actually view, and use that screenshot as the proof.

- Do not use a fullpage screenshot as proof for a floating header, because scrolling in a fullpage capture can falsely make the header look cut off.

- For a looping or animated element, capture the frame where the content is fully visible and state which phase of the loop the frame shows.

- Never present an empty reset frame of an animation as proof that text is missing.

## Check every surface the change touches

- Open every page where the changed element appears and verify the change on each one, not only on the page where you edited it.

- Check the element at mobile width as well as desktop width, and confirm no title is covered and no buttons are stuck together.

- Check colour consistency across pages, so a header that must look different from the page body looks the same on every page where it appears.

- Verify the result on the production surface the user sees, and do not claim the fix is done from a local or staging result alone.

## Present proof before claiming done

- Send the viewport screenshot together with the measured before and after numbers for the properties the user named.

- Name each property that changed and each property that stayed the same, so the user can check your claim against the image.

- Say plainly which surfaces you checked and which surfaces you did not check, instead of implying a whole product was checked.

- Wait for the user verdict on that measured proof before calling the work done or starting a rebuild.

## Available connectors

- Use `muse.connector_search` to find other connectors and `muse.skill_search` to find related skills.

- If nothing here fits, look on the web for a maintained API or MCP server and set it up with [Custom Connectors and MCPs](/opt/muse/skills/custom-connector-setup/SKILL.md), or build a custom connector.

## Alternatives for better results

- Load the ui-ux-pro-max skill for the design rule behind a fix, and use this skill for the measurement and proof that the fix landed.

- Load the pre-publish claim check skill when page copy carries a factual claim, and keep factual verification separate from visual verification.

- Ask the user which page and which device width matters most when the same element looks different across pages, and measure that case first.

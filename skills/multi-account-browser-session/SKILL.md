---
name: multi-account-browser-session
description: Multi Account Browser Sessions
---

# Multi Account Browser Sessions

## Verify the filled identity before you submit

- Read the filled username or email field character by character before you click any login or submit button.

- Type the identifier manually when the filled value belongs to a different account, and use only the saved password for that account.

- Stop after one mismatched autofill instead of retrying the same autofill, because a repeat of the same fill produces the same wrong account.

- Withhold the login when you cannot confirm the filled identifier matches the account you intend to open.

## Settle the opening state before you work

- Read the opening balance, count, or progress value before you do any credited work in that account.

- Compare the opening value with the last confirmed value, and treat any increase as a pending credit that has now landed.

- Report a pending credit as settled only when the opening value proves it, and never count the same credit again in the same session.

- Record the opening value beside the closing value for that account so a later session can settle its own pending credits the same way.

## Work one account to its limit, then close it

- Finish every step for one account before you open the next account, and never interleave two accounts in one browser session.

- Stop credited work when the site itself states the daily limit, and skip any item the site will not credit instead of repeating it.

- Take only the free actions the task allows, and leave paid actions, bonus actions, settings, and surveys untouched unless the user asked for them by name.

- Log out of the finished account and clear the session state before you start the next account, and confirm the next login screen shows no residue from the previous account.

- Report each account separately with its opening value, its confirmed gain, its limit state, and its logout state, and name any credit that is still unconfirmed rather than calling it complete.

## Available connectors

- Use `muse.connector_search` to find other connectors and `muse.skill_search` to find related skills.

- If nothing here fits, look on the web for a maintained API or MCP server and set it up with [Custom Connectors and MCPs](/opt/muse/skills/custom-connector-setup/SKILL.md), or build a custom connector.

## Alternatives for better results

- Start a fresh browser environment when the site shows a block page or a stuck tab, and re-read the opening state before you resume work.

- Ask the user to supply a fresh saved login entry for the affected account when autofill keeps filling the wrong account, and test the new entry once before you continue.

- Split a stalled multi-account run into a separate retry session rather than forcing progress while the site is blocking the current session.

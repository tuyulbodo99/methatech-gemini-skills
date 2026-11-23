---
name: ai-playground-chat-guard
description: AI Playground Chat Guard
---

# AI Playground Chat Guard

## Identify the counterpart before you send

- Check the page for a model name, a playground label, a prompt box, model selection, or chat plus image modes before you send anything.

- Treat the counterpart as an AI model when the page offers a model to chat with and names no human owner, support agent, or contact channel.

- Ask the user one decisive question that names the candidate identity, the channel, and what the counterpart can actually do, then wait for the answer before the first send.

- Do not ask the same identity question again in pieces across many turns after the user has already answered it once.

## Hold secrets and example values

- Never send a password, API key, auth key, token, private key, or live system key to an AI playground chat.

- Explain plainly that a value sent to such a chat persists in that service chat history and that a single use key may be spent by the send.

- Offer a draft for the user to send himself or ask for the human owner name and channel instead of pasting the secret.

- Treat a value marked as an example or shown only as a command pattern as an example, and never use it as a real address, user, or key.

- Read a real value back to the user and confirm it is the real target before acting on it when it arrives after an example.

## Send once and stop when the counterpart cannot act

- Send each message once, read the reply, and stop asking the same counterpart to act on an outside system after it answers only with instructions.

- Say plainly when the counterpart is an AI model, name what it cannot do, and ask the user for the human owner or the direct access route instead of looping.

- Report what the service confirmed and keep the exchange with one owner until its purpose is met or the user needs to decide.

## Available connectors

- Use `muse.connector_search` to find other connectors and `muse.skill_search` to find related skills.

- If nothing here fits, look on the web for a maintained API or MCP server and set it up with [Custom Connectors and MCPs](/opt/muse/skills/custom-connector-setup/SKILL.md), or build a custom connector.

## Alternatives for better results

- Ask the user for the human owner name and contact channel before any send when the page names no human.

- Draft the message for the user to copy and send himself when the recipient or the channel is still unconfirmed.

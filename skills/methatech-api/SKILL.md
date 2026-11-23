---
name: methatech-api
description: Call the MethaTech API to list models and chat with any MethaTech model. Use when a task needs a MethaTech model, the model list, or anything from the MethaTech platform.
---

# MethaTech API

MethaTech is an AI API platform (186 models). All calls are OpenAI-compatible.

## Setup

- API base: `https://api.methatech.eu.org/v1`
- Console (sign up, top up, create keys): `https://console.methatech.eu.org`
- Auth: send your API key as a Bearer token on every call:
  `Authorization: Bearer PASTE_YOUR_METHATECH_API_KEY_HERE`
- Get a key in the console under API Keys. New accounts need a balance of at least Rp10.000 (Paket Tes) before they can create a key. The key is never written in this skill; paste it where the placeholder is.

## List models

```bash
curl https://api.methatech.eu.org/v1/models \
  -H "Authorization: Bearer PASTE_YOUR_METHATECH_API_KEY_HERE"
```

Returns the full catalog (186 models) with ids and owners.

## Chat with a model

```bash
curl https://api.methatech.eu.org/v1/chat/completions \
  -H "Authorization: Bearer PASTE_YOUR_METHATECH_API_KEY_HERE" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "glm-5.3-flash",
    "messages": [{"role": "user", "content": "Halo"}]
  }'
```

Use `"stream": true` for streaming responses.

## Free models (no paid balance needed)

These 10 models are free for every account:

- deepseek-v4-flash
- glm-5.3-flash
- gpt-6-luna
- gemini-3.8-flash
- gpt-6-astra
- gemini-3.1-pro
- qwen3.8-flash
- qwen3.7-max
- kimi-k2.7-code
- deepseek-v4.1-flash

## Pricing

- Paid models are billed per 1M tokens (input/output prices are in the model list).
- $1 = 500,000 quota. New users get $20 free credit once.
- If a call returns 402, the account balance is empty; top up in the console.

## Rules

- Never share your API key. If it leaks, delete it in the console and create a new one.
- Use the exact model id from `/v1/models`. Do not guess model names.
- After any call, report what the API actually returned, not what you expected.

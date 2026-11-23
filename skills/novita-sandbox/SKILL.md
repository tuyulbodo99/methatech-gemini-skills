---
name: novita-sandbox
description: Open a Novita cloud sandbox for special tasks that need a real Linux shell, install software or run commands inside it, then kill it. Use when a task needs an isolated machine instead of the local one.
---

# Novita Sandbox

## When to use

- A task needs installing software, running a script, or testing something in an isolated Linux machine.
- The work must not touch the local machine (install tasks, untrusted code, one-off experiments).

## When NOT to use

- For ordinary chat, writing, or lookups. No sandbox needed.
- For anything that must stay running longer than 1 hour (free sandbox limit).
- Never use it to run anything harmful, to attack systems, or to bypass a site's protections.

## Security

- This file contains a live Novita API key. NEVER share this file and NEVER paste the key anywhere else. If the key leaks, revoke it in the Novita console and replace it here.
- The sandbox is a separate cloud machine. Do not copy other credentials into it unless the task needs them, and kill the sandbox when done.

## Setup

- Python SDK: `pip install novita-sandbox` (version 2.1.4 verified).
- API key, already in this file. Do not ask the user for it:

```python
NOVITA_API_KEY = "PASTE_YOUR_NOVITA_API_KEY_HERE"
```

## Open a sandbox

```python
from novita_sandbox import Sandbox

sandbox = Sandbox.create(
    timeout=3600,  # seconds; free (Hobby) max 3600 = 1 hour, default 300
    api_key=NOVITA_API_KEY,
)
print(sandbox.sandbox_id)  # save this id to reconnect later
```

## Reconnect to a sandbox

```python
from novita_sandbox import Sandbox

sandbox = Sandbox.connect(sandbox_id, api_key=NOVITA_API_KEY)
```

## Run commands

```python
result = sandbox.commands.run("whoami && pwd", timeout=60)
print(result.stdout)
print(result.stderr)
print(result.exit_code)  # 0 means success
```

- Commands run as user `user`, working directory `/` unless `cwd=` is given.
- `timeout=` is per-command seconds (default 60, 0 = no limit).
- Install example: `sandbox.commands.run("pip install <pkg>", timeout=300)`
- Long jobs: pass `background=True` to get a handle instead of waiting.

## Files

- `sandbox.files.write(path, content)` writes a file into the sandbox; `sandbox.files.read(path)` reads one back.
- Save any result you need BEFORE the sandbox dies. A free sandbox lives at most 1 hour.

## Kill it when done

```python
from novita_sandbox import Sandbox

Sandbox.kill(sandbox_id, api_key=NOVITA_API_KEY)
```

Always kill the sandbox when the task is finished. Never leave sandboxes running.

## Troubleshooting

- `AuthenticationException` / 401: the key is wrong or expired. Check the key, do not invent a new one.
- Connection or SSL errors on first try: retry once, the network can be flaky.
- If a sandbox id no longer connects, it already expired. Create a fresh one.

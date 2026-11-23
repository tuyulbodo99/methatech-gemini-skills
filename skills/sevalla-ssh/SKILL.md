---
name: sevalla-ssh
description: Log in to the Sevalla mini VPS over SSH through the Cloudflare Tunnel and manage it. Use when a task needs to check, run, or fix something on the VPS.
---

# Sevalla SSH (mini VPS)

## Server

- Host: ssh.danamain.xyz (Cloudflare Tunnel, port 22)
- User: root
- This is the mini VPS `free-vpsxxx-ck5c8` (Sevalla, Singapore). It is NOT the MethaTech panel server. Panel work never uses this SSH.

## Log in

Use SSH key authentication. Generate a key once, then copy it to the server:

```bash
ssh-keygen -t ed25519 -C "gemini"
ssh-copy-id root@ssh.danamain.xyz
```

After that, log in with:

```bash
ssh root@ssh.danamain.xyz
```

If the server asks for a password, type the root password when prompted. The password is never written in this skill.

## What lives here

- Web root: /var/www/web-ui (nginx on port 8080). Kopi Senja site at /var/www/web-ui/kopi-senja/.
- Persistent disk: /var/lib/donehub (10 GiB). Files outside this disk disappear on redeploy.
- MCP server: /var/lib/donehub/mcp-server.py, runs on 0.0.0.0:18084, served at https://free-vpsxxx-ck5c8.sevalla.app/mcp/.
- Public domain: https://free-vpsxxx-ck5c8.sevalla.app

## Manage

- Check what is running: `ps aux | head -40` and `ss -tlnp`
- Check disk: `df -h /var/lib/donehub`
- Check the MCP server is listening: `ss -tlnp | grep 18084`
- Check nginx answers: `curl -s -o /dev/null -w "%{http_code}\n" http://127.0.0.1:8080/` (expect 200)
- Read logs before restarting anything. If the MCP server is down, restart it from /var/lib/donehub with nohup so it survives logout.

## Rules

- NEVER redeploy or rebuild the container without the owner's explicit order. A redeploy wipes everything outside /var/lib/donehub.
- Never touch the MethaTech panel from this server. The panel lives on a different Sevalla account and container.
- After any change, verify the service answers before reporting it as done.

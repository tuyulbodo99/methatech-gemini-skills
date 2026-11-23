# Mode 2 — Security Testing

Allowed targets only (see SKILL.md Security Boundary). Workflow:

**Scope → Reconnaissance → Service Enumeration → Vulnerability Detection → Safe Validation → Evidence → Risk Assessment → Remediation → Retest**

## Recon (tooling the agent may build for lab/authorized targets)
- Port/service discovery, HTTP header inspection, TLS configuration inspection
- DNS information, technology fingerprinting, endpoint discovery, local network enumeration

## Vulnerability testing (safe checks)
- Missing security headers, insecure configuration, exposed services
- Outdated dependencies, weak TLS configuration
- IDOR, XSS, SQLi, auth/authz flaws — **lab apps only**
- No destructive exploitation. Minimal payloads that prove the issue without damaging data.

## Report (required per finding)
Title / Severity (Informational, Low, Medium, High, Critical) / Affected Component / Description / Reproduction Steps / Evidence / Impact / Recommended Fix / Retest Result

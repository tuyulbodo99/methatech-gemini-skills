# Mode 3 — APK Analysis Tool

For the user's own APK or one explicitly permitted for analysis. Never extract credentials, session tokens, private keys, or user data from third-party apps.

## Workflow
APK → Hash → Metadata → Manifest → Permissions → Certificate → Static Analysis → Dynamic Analysis → Network Observation → Report

## Capabilities to implement
- Metadata: package name, version, hash (sha256)
- Manifest inspection, permissions analysis, exported component detection
- Certificate/signature inspection (`apksigner verify --print-certs`)
- Strings extraction, resource inspection, network endpoint discovery
- Static code analysis where tooling allows

## Tooling (use if present, else user-space install)
`adb`, `aapt`/`aapt2`, `apktool`, `jadx`, `apksigner`, `apkanalyzer`, Android SDK, Frida, Objection, MobSF.

Dynamic analysis only on the user's own emulator/device.

## Test matrix
Valid APK, corrupted APK, APK with no permissions, APK with many permissions, APK with exported components.

# Environment Audit, Testing & Debugging

## Audit (run before building)
```bash
uname -a; cat /etc/os-release
python3 --version; node --version; npm --version; java -version; adb version; git --version
for b in python3 node npm adb apktool jadx curl wget; do which $b; done
```
Missing deps → package manager or user-space install; virtualenv where possible. Never destructively alter system config; no root assumed.

## Automated testing (minimum per tool)
Input validation, happy path, invalid input, network timeout, empty response, malformed response, permission error, file error. Scraper/APK matrices live in their mode files.

## Debugging playbook
1. Capture the error 2. Identify root cause 3. Check dependencies 4. Check permissions 5. Reproduce minimally 6. Apply the smallest fix 7. Re-run tests 8. Document the solution

Report failures as:
```
ERROR: <what failed>
CAUSE: <root cause>
FIX: <what was changed>
TEST RESULT: <outcome>
```

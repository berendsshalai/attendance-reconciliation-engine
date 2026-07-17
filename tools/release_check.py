from __future__ import annotations

import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def main() -> int:
    checks = [
        [sys.executable, "tools/privacy_gate.py"],
        [sys.executable, "-m", "compileall", "src"],
        [sys.executable, "-m", "pytest", "tests"],
    ]
    for check in checks:
        print("+", " ".join(check))
        result = subprocess.run(check, cwd=ROOT)
        if result.returncode:
            return result.returncode
    print("release checks passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

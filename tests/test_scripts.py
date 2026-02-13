from __future__ import annotations

import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def run_script(*args: str, cwd: Path | None = None) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        [sys.executable, *args],
        cwd=str(cwd or ROOT),
        text=True,
        capture_output=True,
        check=False,
    )


def test_domain_verify_passes() -> None:
    result = run_script("scripts/domain_verify.py")
    assert result.returncode == 0, result.stdout + result.stderr
    assert "OK: domain verification passed" in result.stdout


def test_validate_contracts_passes() -> None:
    result = run_script("scripts/validate_contracts.py")
    assert result.returncode == 0, result.stdout + result.stderr
    assert "OK: contracts validated for rooms.md" in result.stdout


def test_check_unique_info_detects_missing_token(tmp_path: Path) -> None:
    source = tmp_path / "source.md"
    canonical = tmp_path / "canonical.md"

    source.write_text(
        "### R01 — Room\n"
        "- **Description (EN)**: Unique phrase only in source\n",
        encoding="utf-8",
    )
    canonical.write_text(
        "### R01 — Room\n"
        "- **Description (EN)**: Common phrase\n",
        encoding="utf-8",
    )

    missing = run_script(
        "scripts/check_unique_info.py",
        "--source",
        str(source),
        "--canonical",
        str(canonical),
    )
    assert missing.returncode == 2
    assert "MISSING_TOKENS:" in missing.stdout


def test_check_unique_info_normalizes_aliases(tmp_path: Path) -> None:
    source = tmp_path / "source.md"
    canonical = tmp_path / "canonical.md"

    source.write_text(
        "| ID | View | Floor | Area |\n"
        "| -- | -- | -- | -- |\n"
        "| **01** | Piscine (Accès direct) | RDC | 40m2 |\n"
        "### [01] Deluxe\n"
        "- **Features**: Piscine + Acces direct piscine\n",
        encoding="utf-8",
    )
    canonical.write_text(
        "| Room ID | View | Floor | Size (m²) |\n"
        "| ------- | ---- | ----- | --------- |\n"
        "| R01 | Pool view (direct access) | Ground Floor | 40 m² |\n"
        "### R01 — Deluxe\n"
        "- **Legacy Features (Alias)**: Pool access (direct)\n",
        encoding="utf-8",
    )

    clear = run_script(
        "scripts/check_unique_info.py",
        "--source",
        str(source),
        "--canonical",
        str(canonical),
    )
    assert clear.returncode == 0, clear.stdout + clear.stderr
    assert "MISSING_TOKENS: 0" in clear.stdout

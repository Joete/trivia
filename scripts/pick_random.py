#!/usr/bin/env python3
"""
pick_random.py
--------------
Liest data/entries.json, wählt zufällig einen Eintrag aus und schreibt
das Ergebnis als result.json in das Root-Verzeichnis des Repos.

Wird von der GitHub Action aufgerufen (siehe .github/workflows/daily-pick.yml).
Kann aber auch lokal ausgeführt werden:
    python scripts/pick_random.py
"""

import json
import random
from datetime import datetime, timezone
from pathlib import Path

# Pfade relativ zum Repo-Root (Script liegt in scripts/)
REPO_ROOT   = Path(__file__).parent.parent
ENTRIES_FILE = REPO_ROOT / "data" / "entries.json"
RESULT_FILE  = REPO_ROOT / "result.json"


def main() -> None:
    # --- Einträge laden ---
    with ENTRIES_FILE.open(encoding="utf-8") as f:
        data = json.load(f)

    entries = data.get("entries", [])
    if not entries:
        raise ValueError("Keine Einträge in data/entries.json gefunden.")

    # --- Zufällig einen auswählen ---
    chosen = random.choice(entries)

    # --- Ergebnis-JSON zusammenstellen ---
    result = {
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "total_entries": len(entries),
        "result": chosen
    }

    # --- Schreiben ---
    with RESULT_FILE.open("w", encoding="utf-8") as f:
        json.dump(result, f, ensure_ascii=False, indent=2)

    print(f"✓ result.json aktualisiert → Eintrag #{chosen.get('id')}: {chosen.get('title')}")


if __name__ == "__main__":
    main()

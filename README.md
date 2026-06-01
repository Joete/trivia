# Random Pick Service · GitHub Pages

Ein minimaler statischer "Webservice", der täglich einen zufälligen Eintrag aus einer Liste wählt und als JSON-Endpunkt bereitstellt — komplett ohne Server, gehostet auf GitHub Pages.

---

## Architektur

```
repo/
├── data/
│   └── entries.json          ← Deine ~200 Einträge (editierbar)
├── scripts/
│   └── pick_random.py        ← Wählt zufällig einen Eintrag aus
├── .github/
│   └── workflows/
│       └── daily-pick.yml    ← GitHub Action (täglich 06:00 UTC)
├── result.json               ← API-Endpunkt (auto-generiert)
└── index.html                ← Dashboard
```

**Endpunkt:** `https://<username>.github.io/<repo>/result.json`

---

## Setup (5 Minuten)

### 1. Repo erstellen & pushen

```bash
git init
git add .
git commit -m "init: random pick service"
git remote add origin https://github.com/<username>/<repo>.git
git push -u origin main
```

### 2. GitHub Pages aktivieren

Repo → **Settings → Pages → Source: Deploy from branch → main / (root)**

### 3. Action-Permissions setzen

Repo → **Settings → Actions → General → Workflow permissions → Read and write permissions** ✓

Das ist nötig damit die Action `result.json` committen kann.

### 4. Ersten Pick manuell auslösen

Repo → **Actions → Daily Random Pick → Run workflow**

Danach läuft alles automatisch täglich.

---

## Einträge pflegen

Editiere `data/entries.json`. Jeder Eintrag ist ein JSON-Objekt — die Felder sind völlig frei:

```json
{
  "entries": [
    { "id": 1, "title": "Mein Eintrag", "kategorie": "X", "wert": 42 },
    { "id": 2, "title": "Noch ein Eintrag", "kategorie": "Y", "tags": ["a", "b"] }
  ]
}
```

Bei einem Push auf `main` mit Änderungen an `data/entries.json` wird automatisch ein neuer Pick gezogen.

---

## result.json Format

```json
{
  "generated_at": "2026-06-01T06:00:00+00:00",
  "total_entries": 200,
  "result": {
    "id": 42,
    "title": "Zufälliger Eintrag",
    "...": "..."
  }
}
```

---

## Lokaler Test

```bash
python scripts/pick_random.py
# ✓ result.json aktualisiert → Eintrag #7: Eintrag Eta
```

Dann `index.html` im Browser öffnen (via lokalem Server, z.B. `python -m http.server`).

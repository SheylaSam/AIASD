# Setup-Guide für Teammitglieder

> Damit ihr auf dem gleichen Stand seid wie Sheyla: Claude Code installieren, Repo klonen, Demo ausprobieren.

---

## Übersicht: Was ihr braucht

| Tool | Zweck |
|---|---|
| **Git** | Repo klonen und gemeinsam arbeiten |
| **Node.js** | Voraussetzung für Claude Code |
| **Claude Code** | Das CLI-Tool, das wir pitchen |
| **Anthropic-Account** | Für API-Zugang / Abo |

---

## Schritt 1: Repo klonen

```bash
git clone https://github.com/SheylaSam/AIASD.git
cd AIASD
```

---

## Schritt 2: Node.js installieren (falls nicht vorhanden)

Claude Code benötigt Node.js 18 oder neuer.

**Prüfen ob bereits vorhanden:**
```bash
node --version   # sollte v18 oder höher zeigen
```

**Falls nicht installiert:**
- macOS: [nodejs.org/de](https://nodejs.org/de) > "LTS" herunterladen und installieren
- Windows: Gleiche Seite, Windows-Installer
- Oder via Homebrew (macOS): `brew install node`

---

## Schritt 3: Claude Code installieren

```bash
npm install -g @anthropic-ai/claude-code
```

**Prüfen ob es funktioniert hat:**
```bash
claude --version
```

---

## Schritt 4: Anthropic-Account und API-Zugang

### Option A: Claude Pro Abo (empfohlen, einfacher)
1. Auf [claude.ai](https://claude.ai) anmelden / registrieren
2. Auf **Claude Pro** upgraden ($20/Monat, jederzeit kündbar)
3. Claude Code ist dann inklusive, kein separater API-Key nötig

### Option B: API-Key (günstiger bei wenig Nutzung)
1. Account erstellen auf [console.anthropic.com](https://console.anthropic.com)
2. Unter **API Keys** > "Create Key" einen neuen Key erstellen
3. Etwas Guthaben aufladen (min. $5, reicht für viele Wochen)
4. Key als Umgebungsvariable setzen:

```bash
# macOS / Linux, in ~/.zshrc oder ~/.bashrc einfügen:
export ANTHROPIC_API_KEY="sk-ant-..."

# Windows (PowerShell):
$env:ANTHROPIC_API_KEY="sk-ant-..."
```

> **Tipp:** Für die Demo und den Pitch reicht das Minimum-Guthaben locker, die Demo verbraucht nur wenige Cent.

---

## Schritt 5: Claude Code starten

```bash
cd AIASD
claude
```

Beim ersten Start wirst du durch die Authentifizierung geführt (Browser öffnet sich automatisch bei Option A).

---

## Demo ausprobieren

Sobald `claude` läuft, diesen Prompt eingeben:

```
Lies content.json und erstelle daraus ein spielbares Memory-Spiel
als memory.html. Schönes modernes Design, 4x4 Grid, Karten mit
Flip-Animation, Punktestand und Gewinn-Anzeige.
```

Danach:
```bash
open memory.html      # macOS
start memory.html     # Windows
```

---

## Dateien im Repo

```
AIASD/
├── content.json           <- Lerninhalt (8 AISD-Begriffe, hier anpassen!)
├── memory.html            <- Fertig generiertes Memory-Spiel (Backup)
├── Claude_Code_Pitch.pptx <- Präsentation für den Pitch
├── README.md              <- Projektübersicht
└── SETUP.md               <- Diese Datei
```

---

---

## Backend starten (FastAPI)

### Voraussetzung: Python 3.10 via pyenv

**pyenv installieren (falls nicht vorhanden):**
```bash
brew install pyenv
echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.zshrc
echo 'export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.zshrc
echo 'eval "$(pyenv init -)"' >> ~/.zshrc
source ~/.zshrc
```

**Python 3.10.13 installieren:**
```bash
pyenv install 3.10.13
```

### Backend starten

```bash
cd backend
pyenv local 3.10.13          # Python-Version setzen (einmalig pro Ordner)
python3 -m pip install -r requirements.txt   # Pakete installieren (einmalig)
PYTHONPATH=. python3 -m uvicorn main:app --reload
```

API läuft dann auf: **http://localhost:8000**
Interaktive Dokumentation: **http://localhost:8000/docs**

### Tests ausführen

```bash
cd backend
python3 -m pytest
```

Alle 16 Tests laufen automatisch durch und zeigen ob alles funktioniert.

**Was getestet wird:**

| Test-Datei | Was wird geprüft |
|---|---|
| `test_domain_user.py` | User erstellen, leerer Name wirft Fehler, ungültige Email wirft Fehler |
| `test_domain_quiz.py` | QuizFrage erstellen, zu wenige Antworten wirft Fehler, ungültiger Index wirft Fehler |
| `test_user_service.py` | User registrieren, doppelte Email wirft Fehler, User per ID abrufen, nicht-existente ID wirft Fehler, alle Users auflisten |
| `test_user_repository.py` | User in DB speichern und laden, per Email finden, nicht-existente ID gibt None, alle Users aus DB laden |

Erwartete Ausgabe wenn alles funktioniert:
```
16 passed in 0.19s
```

### Umgebungsvariablen (optional)

Für PostgreSQL (Prod) statt SQLite (Dev):
```bash
export DATABASE_URL="postgresql://user:password@localhost/aiasd"
```

Ohne diese Variable wird automatisch SQLite (`app.db`) verwendet.

---

## Probleme?

| Problem | Lösung |
|---|---|
| `claude: command not found` | Terminal neu starten nach npm install |
| `permission denied` bei npm | `sudo npm install -g @anthropic-ai/claude-code` |
| API-Key wird nicht erkannt | Terminal neu starten, Schreibweise prüfen |
| Windows: Fehler beim Start | WSL installieren (Windows Subsystem for Linux) und dort starten |

Oder einfach Sheyla fragen :)

---

*Viel Erfolg beim Pitch! · FHNW AISD 2026*

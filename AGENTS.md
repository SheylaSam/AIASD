# AGENTS.md — AIASD Lernplattform

AI-Assisted Lean SDLC mit Clean Architecture, TDD & CI/CD.
Funktioniert mit Claude Code, GitHub Copilot, Cursor, Windsurf und Cline.

## Projekt

Kollaborative Lernplattform: Nutzerinnen laden PDFs hoch, KI generiert daraus Lernpläne und Quizzes. Gruppen lernen gemeinsam in einem LernRaum.

- **Tech Stack:** FastAPI (Python), SQLAlchemy, SQLite/PostgreSQL, n8n, Claude API
- **Repo:** https://github.com/SheylaSam/AIASD

## Architektur

Clean Architecture — Abhängigkeiten zeigen immer nach innen:

```
Infrastructure  (FastAPI, SQLAlchemy, n8n)
    ↓
Interfaces      (API-Routes, Schemas)
    ↓
Application     (Use Cases, Repository-Ports)
    ↓
Domain          (User, Document, Quiz, LernRaum)
```

Details: `docs/CLEAN_ARCH.md`

## Workflow-Phasen (AI-SDLC)

1. **SPECIFY** — Use Cases in `docs/specs/` definieren
2. **DESIGN** — Architektur & Test-Strategie (`docs/CLEAN_ARCH.md`)
3. **DEVELOP** — TDD: Integration → Unit → Code (`docs/TDD.md`)
4. **VALIDATE** — Vollständige Test-Pyramide ausführen
5. **DEPLOY** — Docker + CI/CD

Details: `docs/PHASES.md`

## Globale Regeln

- Tests vor Code (TDD: Red → Green → Refactor)
- Jede neue Funktion braucht Unit Tests in `backend/tests/unit/`
- Abhängigkeiten zeigen nach innen — nie Infrastructure in Domain importieren
- Kommentare und Dokumentation auf Deutsch, Code auf Englisch
- Commit-Messages auf Deutsch, imperativ (z.B. "User-Registrierung hinzufügen")

## Commands

```bash
# Backend starten
cd backend && PYTHONPATH=. python3 -m uvicorn main:app --reload

# Tests ausführen
cd backend && python3 -m pytest

# Nur Unit Tests
cd backend && python3 -m pytest tests/unit/

# Nur Integration Tests
cd backend && python3 -m pytest tests/integration/
```

## Skills

Für Claude Code verfügbar unter `.claude/skills/`:

| Skill | Befehl | Zweck |
|---|---|---|
| New Feature | `/new-feature` | Branch, Scaffold und Issue verknüpfen |
| Tests | `/run-tests` | Alle Tests ausführen und auswerten |
| Deploy | `/deploy` | Auf Staging oder Produktion deployen |
| n8n Workflow | `/n8n-workflow` | Neuen n8n Workflow anlegen |
| DB Migration | `/db-migrate` | Datenbankmigrationen erstellen |

# AIASD Capstone: Kollaborative Lernplattform

## Projektübersicht

Eine Web-App, bei der Nutzerinnen Lerninhalt (PDF, Folien) hochladen können. Die KI erstellt daraus automatisch einen Lernplan und Quizzes. Gruppen können gemeinsam in einem Lernraum lernen und den Fortschritt verfolgen.

Entwickelt im Rahmen des Kurses AI-Assisted Software Development (FHNW, 2026).

## Tech Stack

| Schicht | Technologie |
|---|---|
| Frontend | HTML/JS oder React |
| Backend API | FastAPI (Python) |
| Workflow-Engine | n8n (KI-Verarbeitung) |
| Datenbank | SQLite (Dev) / PostgreSQL (Prod) |
| KI | Claude API via n8n Anthropic-Node |
| Deployment | Docker + Render/Railway |
| CI/CD | GitHub Actions |

## Architektur

```
Frontend
    |
FastAPI Backend  <-->  Datenbank (PostgreSQL)
    |
n8n Webhook
    |
n8n Workflow:
  1. PDF-Text extrahieren
  2. Claude API aufrufen
  3. Quiz + Lernplan als JSON parsen
  4. Ergebnis an Backend zurückschicken
```

## Projektstruktur

```
AIASD/
├── backend/
│   ├── app/
│   │   ├── domain/          # Entities (User, Document, Quiz, LernRaum)
│   │   ├── application/     # Use Cases und Business Logic
│   │   ├── interfaces/      # API Routes (FastAPI)
│   │   └── infrastructure/  # DB, Config, externe Services
│   ├── tests/
│   │   ├── unit/
│   │   └── integration/
│   └── main.py
├── frontend/
├── n8n/                     # n8n Workflow-Exports (JSON)
├── .claude/
│   └── skills/              # Claude Code Skills
├── CLAUDE.md                # Diese Datei
└── docker-compose.yml
```

## Coding Conventions

- Sprache: Deutsch für Kommentare und Dokumentation, Englisch für Code
- Branch-Naming: `feature/kurze-beschreibung`, `fix/was-wird-gefixt`
- Commit-Messages: auf Deutsch, imperativ (z.B. "Authentifizierung hinzufügen")
- Jeder Branch hat ein zugehöriges GitHub Issue
- Vor dem Merge: mindestens ein Review von einer anderen Person
- Tests sind Pflicht für neue Backend-Features

## Verfügbare Skills

| Skill | Befehl | Zweck |
|---|---|---|
| New Feature | `/new-feature` | Branch, Scaffold und Issue verknüpfen |
| Tests | `/run-tests` | Alle Tests ausführen und auswerten |
| Deploy | `/deploy` | Auf Staging oder Produktion deployen |
| n8n Workflow | `/n8n-workflow` | Neuen n8n Workflow anlegen |
| DB Migration | `/db-migrate` | Datenbankmigrationen erstellen und ausführen |

## GitHub

- Repo: https://github.com/SheylaSam/AIASD
- Scrum-Board: https://github.com/users/SheylaSam/projects/3
- Issues: https://github.com/SheylaSam/AIASD/issues

## Team

| Person | Bereich |
|---|---|
| Sheyla | n8n Workflows und Claude API Integration |
| Person 2 | Frontend |
| Person 3 | Backend API (FastAPI) und Datenbank |
| Person 4 | Auth, Testing und Deployment |

## Sprints

| Sprint | Thema | Deadline |
|---|---|---|
| Sprint 1 | Setup und Grundstruktur | 16. März |
| Sprint 2 | Upload und KI-Generierung | 30. März |
| Sprint 3 | Lernraum und Gruppen | 13. April |
| Sprint 4 | Polish und Deployment | 27. April |

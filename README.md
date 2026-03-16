# AIASD: Kollaborative Lernplattform

> FHNW · BSc Business Artificial Intelligence · 4. Semester · 2026
> Kurs: AI-Assisted Software Development (Prof. Dr. Andreas Martin)

---

## Projektbeschreibung

Eine Web-App, bei der Nutzer:innen Lernmaterial (PDF, Folien) hochladen können. Die KI erstellt daraus automatisch einen Lernplan und Quizzes. Gruppen können gemeinsam in einem LernRaum lernen und den Fortschritt verfolgen.

---

## Tech Stack

| Schicht | Technologie |
|---|---|
| Frontend | HTML/JS oder React |
| Backend API | FastAPI (Python) |
| Workflow-Engine | n8n (KI-Verarbeitung) |
| Datenbank | SQLite (Dev) / PostgreSQL (Prod) |
| KI | Claude API via n8n |
| Deployment | Docker + Render/Railway |

---

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

Details: [docs/CLEAN_ARCH.md](docs/CLEAN_ARCH.md)

---

## Schnellstart

```bash
git clone https://github.com/SheylaSam/AIASD.git
cd AIASD/backend
pyenv local 3.10.13
python3 -m pip install -r requirements.txt
PYTHONPATH=. python3 -m uvicorn main:app --reload
```

API läuft auf **http://localhost:8000** · Dokumentation: **http://localhost:8000/docs**

Vollständige Anleitung: [SETUP.md](SETUP.md)

---

## Tests

```bash
cd backend
python3 -m pytest
```

16 automatische Tests (Unit + Integration). Alle müssen grün sein vor einem Merge.

---

## Team

| Person | Bereich |
|---|---|
| Sheyla | n8n Workflows und Claude API Integration |
| Andrea | Frontend |
| Fabia | Backend API (FastAPI) und Datenbank |
| Nicolas | Auth, Testing und Deployment |

---

## Sprints

| Sprint | Thema | Deadline |
|---|---|---|
| Sprint 1 | Setup und Grundstruktur | 16. März |
| Sprint 2 | Upload und KI-Generierung | 30. März |
| Sprint 3 | Lernraum und Gruppen | 13. April |
| Sprint 4 | Polish und Deployment | 27. April |

---

## Links

- [Scrum-Board](https://github.com/users/SheylaSam/projects/3)
- [Issues](https://github.com/SheylaSam/AIASD/issues)
- [AGENTS.md](AGENTS.md) — Instruktionen für AI-Coding-Tools
- [docs/](docs/) — Architektur, TDD-Regeln, Workflow-Phasen

---

*Erstellt mit Claude Code · FHNW 2026*

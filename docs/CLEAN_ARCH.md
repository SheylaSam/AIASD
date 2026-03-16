# Clean Architecture — AIASD

## Schichten-Übersicht

| Schicht | Ordner | Inhalt | Darf importieren |
|---|---|---|---|
| Domain | `app/domain/` | User, Document, Quiz, LernRaum | nichts |
| Application | `app/application/` | Services, Repository-Ports (ABCs) | nur Domain |
| Interfaces | `app/interfaces/` | FastAPI-Routes, Pydantic-Schemas | Application + Domain |
| Infrastructure | `app/infrastructure/` | SQLAlchemy-Models, Repositories, DB | alle Schichten |

## Dependency Rule

**Niemals nach aussen importieren.** Domain kennt niemanden. Infrastructure kennt alle.

```
# Erlaubt:
from app.domain.user import User                          # in application/
from app.application.ports.user_repository import ...    # in infrastructure/

# Verboten:
from app.infrastructure.models import UserModel           # in domain/ ← NEIN
from app.interfaces.schemas import UserResponse           # in application/ ← NEIN
```

## Ordnerstruktur

```
backend/
├── main.py
├── app/
│   ├── domain/
│   │   ├── user.py
│   │   ├── document.py
│   │   ├── quiz.py
│   │   └── lernraum.py
│   ├── application/
│   │   ├── ports/
│   │   │   ├── user_repository.py      ← ABC
│   │   │   ├── document_repository.py
│   │   │   ├── quiz_repository.py
│   │   │   └── lernraum_repository.py
│   │   └── services/
│   │       ├── user_service.py
│   │       └── document_service.py
│   ├── interfaces/
│   │   ├── schemas.py
│   │   ├── user_router.py
│   │   └── document_router.py
│   └── infrastructure/
│       ├── database.py
│       ├── models.py
│       └── repositories/
│           ├── user_repository.py      ← SQLAlchemy-Implementierung
│           └── document_repository.py
└── tests/
    ├── unit/
    └── integration/
```

## Neues Feature hinzufügen — Checkliste

1. Domain-Entity in `app/domain/` erstellen oder erweitern
2. Repository-Port (ABC) in `app/application/ports/` definieren
3. Service (Use Case) in `app/application/services/` implementieren
4. SQLAlchemy-Model in `app/infrastructure/models.py` ergänzen
5. SQLAlchemy-Repository in `app/infrastructure/repositories/` erstellen
6. FastAPI-Router in `app/interfaces/` erstellen
7. Router in `main.py` registrieren
8. Unit Tests + Integration Tests schreiben

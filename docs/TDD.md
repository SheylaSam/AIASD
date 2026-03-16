# Test-Driven Development (TDD)

## Red → Green → Refactor

1. **Red** — Test schreiben der fehlschlägt (Funktion existiert noch nicht)
2. **Green** — minimalen Code schreiben bis Test grün ist
3. **Refactor** — Code aufräumen, Tests müssen weiterhin grün bleiben

## Testing-Pyramide

```
        /\
       /E2E\         ← wenige, langsam (API-Endpoints)
      /------\
     /Integr. \      ← einige, mittel (Repository + DB)
    /----------\
   / Unit Tests \    ← viele, schnell (Domain + Services)
  /--------------\
```

## Regeln

- Unit Tests: kein DB, kein FastAPI — nur Domain-Objekte und Services mit Fake-Repositories
- Integration Tests: echte SQLite In-Memory-DB, kein FastAPI
- E2E Tests: FastAPI TestClient gegen echte DB

## Wo liegen die Tests?

```
backend/tests/
├── unit/
│   ├── test_domain_user.py
│   ├── test_domain_quiz.py
│   └── test_user_service.py
├── integration/
│   └── test_user_repository.py
└── e2e/                          ← kommt in Sprint 2
```

## Fake-Repository Pattern

Für Unit Tests kein SQLAlchemy nötig — einfach eine In-Memory-Implementierung:

```python
class FakeUserRepository(UserRepository):
    def __init__(self):
        self._users = {}
        self._next_id = 1

    def save(self, user):
        user.id = self._next_id
        self._users[self._next_id] = user
        self._next_id += 1
        return user
```

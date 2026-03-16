# AI-SDLC Workflow-Phasen

## Phase 0: Bootstrap
Projekt initialisieren: Repo, AGENTS.md, Ordnerstruktur, CI/CD-Pipeline.

## Phase 1: Specify
Use Cases als Markdown in `docs/specs/` definieren.
- Wer macht was? (Akteur)
- Was passiert? (Ablauf)
- Was kann schiefgehen? (Fehlerfall)

Beispiel: `docs/specs/uc-01-user-registrierung.md`

## Phase 2: Design
- Architektur festlegen (`docs/CLEAN_ARCH.md`)
- Test-Strategie definieren (welche Tests für welchen Use Case)
- Tasks aufteilen (`docs/tasks/`)

## Phase 3: Develop (TDD)
Reihenfolge einhalten:
1. Integration Tests schreiben (`tests/integration/`)
2. Unit Tests schreiben (`tests/unit/`)
3. Implementierung schreiben bis Tests grün sind
4. Refactor

Details: `docs/TDD.md`

## Phase 4: Validate
```bash
python3 -m pytest          # Alle Tests
python3 -m pytest tests/unit/         # Nur Unit
python3 -m pytest tests/integration/ # Nur Integration
```

CI/CD führt Tests automatisch bei jedem Push aus.

## Phase 5: Deploy
Docker-Container bauen und auf Render/Railway deployen.

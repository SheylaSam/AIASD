# Skill: new-feature

Erstellt einen neuen Feature-Branch, legt die passenden Dateien an und verknüpft alles mit dem GitHub Issue.

## Verwendung

```
/new-feature
```

## Workflow

1. Frage nach der Issue-Nummer und dem Featurenamen
2. Erstelle einen Branch: `feature/issue-{nr}-{name}`
3. Lege die nötigen Dateien an je nach Bereich:
   - Backend: Route in `backend/app/interfaces/api/`, Use Case in `backend/app/application/`, Entity in `backend/app/domain/` falls nötig
   - Frontend: Neue Seite oder Komponente in `frontend/`
   - n8n: Neuen Workflow-Export in `n8n/`
4. Erstelle leere Testdatei in `backend/tests/`
5. Verknüpfe den Branch mit dem GitHub Issue

## Konventionen

- Branch-Name: `feature/issue-{nr}-kurze-beschreibung` (Kleinbuchstaben, Bindestriche)
- Erste Commit-Message: `Feature #{nr}: {Beschreibung} starten`
- Immer eine leere Testdatei miterstellen

## Beispiel

```
Issue #5: "Als Nutzerin möchte ich ein Dokument hochladen"
Branch:   feature/issue-5-dokument-hochladen
Dateien:  backend/app/interfaces/api/document_api.py
          backend/app/application/document_use_cases.py
          backend/tests/unit/test_document_use_cases.py
          frontend/pages/upload.html
```

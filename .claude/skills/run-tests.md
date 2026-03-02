# Skill: run-tests

Führt die Testsuite aus, wertet die Ergebnisse aus und schlägt Fixes vor bei Fehlern.

## Verwendung

```
/run-tests
```

## Workflow

1. Setze PYTHONPATH korrekt: `export PYTHONPATH=$PWD/backend/src`
2. Führe Unit Tests aus: `pytest -q backend/tests/unit`
3. Führe Integration Tests aus: `pytest -q backend/tests/integration`
4. Zeige eine Zusammenfassung: wie viele Tests bestanden, wie viele fehlgeschlagen
5. Bei Fehlern: Analysiere die Fehlermeldung und schlage einen Fix vor

## Optionen

- Nur Unit Tests: `pytest -q backend/tests/unit`
- Nur Integration Tests: `pytest -q backend/tests/integration`
- Mit Coverage: `pytest --cov=app backend/tests/`
- Einzelne Datei: `pytest backend/tests/unit/test_xyz.py`

## Hinweise

- Integration Tests benötigen eine laufende Datenbankverbindung
- Umgebungsvariable `DATABASE_URL=sqlite:///:memory:` für schnelle lokale Tests setzen
- Vor jedem Merge auf main müssen alle Tests bestehen

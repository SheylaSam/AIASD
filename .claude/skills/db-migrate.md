# Skill: db-migrate

Erstellt und führt Datenbankmigrationen aus.

## Verwendung

```
/db-migrate
```

## Workflow

1. Frage was sich am Schema geändert hat (neue Tabelle, neues Feld, etc.)
2. Erstelle die Migration mit Alembic: `alembic revision --autogenerate -m "beschreibung"`
3. Prüfe die generierte Migrationsdatei in `backend/alembic/versions/`
4. Führe die Migration aus: `alembic upgrade head`
5. Bestätige dass die Datenbank aktuell ist: `alembic current`

## Wichtige Befehle

```bash
# Neue Migration erstellen
alembic revision --autogenerate -m "nutzer tabelle hinzufuegen"

# Migrationen anwenden
alembic upgrade head

# Eine Migration zurück
alembic downgrade -1

# Aktuellen Stand prüfen
alembic current

# Migrationshistorie anzeigen
alembic history
```

## Datenbank-Schema (Überblick)

| Tabelle | Inhalt |
|---|---|
| `users` | Nutzerinnen (id, email, passwort_hash, erstellt_am) |
| `documents` | Hochgeladene Dokumente (id, user_id, dateiname, status) |
| `quizzes` | Generierte Quizzes (id, document_id, fragen als JSON) |
| `lernplaene` | Generierte Lernpläne (id, document_id, inhalt als JSON) |
| `lernraeume` | Gruppenräume (id, name, einladungslink, erstellt_von) |
| `lernraum_mitglieder` | Mitgliedschaften (lernraum_id, user_id) |
| `fortschritt` | Quiz-Ergebnisse (user_id, quiz_id, punkte, abgeschlossen_am) |

## Hinweise

- Migrations-Dateien immer committen
- Niemals bestehende Migrationen ändern, nur neue erstellen
- In Produktion: Migration vor dem Deployment ausführen

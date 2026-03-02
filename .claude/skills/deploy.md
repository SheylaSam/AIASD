# Skill: deploy

Führt den Deployment-Workflow auf Staging oder Produktion durch.

## Verwendung

```
/deploy
```

## Workflow

1. Frage nach Zielumgebung: `staging` oder `production`
2. Prüfe ob alle Tests bestehen (`/run-tests`)
3. Prüfe ob es uncommitted Changes gibt (`git status`)
4. Baue den Docker-Container: `docker build -t aiasd .`
5. Pushe auf die Zielumgebung:
   - Staging: `git push origin main` (löst GitHub Actions aus)
   - Production: manuelles Deployment via Render Deploy Hook

## Voraussetzungen

- Docker ist installiert und läuft
- Umgebungsvariablen sind in `.env` gesetzt (nie committen!)
- GitHub Actions Workflow ist in `.github/workflows/ci.yml` konfiguriert

## Umgebungsvariablen

```
DATABASE_URL=postgresql://...
ANTHROPIC_API_KEY=sk-ant-...
N8N_WEBHOOK_URL=https://...
SECRET_KEY=...
```

## Hinweise

- Niemals direkt auf `main` pushen ohne Tests
- `.env` Datei ist in `.gitignore`, nie committen
- Bei Produktions-Deployment: zuerst auf Staging testen

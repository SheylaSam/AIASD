# Skill: n8n-workflow

Legt einen neuen n8n Workflow an, exportiert ihn und dokumentiert ihn im Repo.

## Verwendung

```
/n8n-workflow
```

## Workflow

1. Frage nach dem Namen und Zweck des Workflows
2. Erstelle eine Dokumentationsdatei in `n8n/{name}.md` mit:
   - Beschreibung des Workflows
   - Trigger (Webhook, Schedule, manuell)
   - Nodes und ihre Reihenfolge
   - Erwarteter Input und Output (JSON-Struktur)
3. Erstelle einen Platzhalter für den n8n-Export in `n8n/{name}.json`
4. Weise darauf hin, den fertigen Workflow aus n8n als JSON zu exportieren und die Datei zu ersetzen

## Bestehende Workflows

| Datei | Zweck |
|---|---|
| `n8n/pdf-verarbeitung.json` | PDF hochladen, Text extrahieren |
| `n8n/quiz-generierung.json` | Text an Claude API schicken, Quiz und Lernplan erhalten |

## n8n Anthropic-Node

Der Anthropic-Node in n8n erlaubt direkte Aufrufe an die Claude API:
- Modell: `claude-sonnet-4-6` (empfohlen)
- API Key: als n8n Credential hinterlegen (nie im Code)
- Output: direkt als JSON weiterverarbeitbar im nächsten Node

## Webhook-URL

Der n8n Webhook nimmt Anfragen vom FastAPI-Backend entgegen:
```
POST {N8N_WEBHOOK_URL}/webhook/dokument-verarbeiten
Body: { "dokument_id": "...", "text": "..." }
```

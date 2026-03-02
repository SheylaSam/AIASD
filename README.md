# AIASD: AI-Assisted Software Development

> **Coding-Agent-Pitch: Claude Code**
> FHNW · BSc Business Artificial Intelligence · 4. Semester · 2026

---

## Was ist das hier?

Dieses Repo entstand als Teil eines **5-minütigen Pitches** über [Claude Code](https://claude.ai/code) im Kurs *AI-Assisted Software Development* (FHNW).

Es enthält:
- Die **Live-Demo**: Ein Memory-Spiel, das Claude Code aus einer simplen JSON-Datei generiert hat
- Den **Inhalt** (`content.json`) mit 8 Begriffen aus dem AISD-Kurs
- Das generierte **Memory-Spiel** (`memory.html`), direkt im Browser spielbar

---

## Demo selbst ausprobieren

```bash
git clone https://github.com/SheylaSam/AIASD.git
cd AIASD
open memory.html   # macOS
# oder: start memory.html (Windows)
```

---

## Das Konzept: Content-First

Die Idee hinter der Demo:

```
content.json  ->  Claude Code  ->  memory.html (spielbar)
    |                                    |
Lerninhalt                      Fertiges Lernspiel
```

Derselbe `content.json` könnte auch für ein Quiz, Flashcards oder andere Lernformate genutzt werden. Claude Code generiert das jeweilige Format auf Anfrage.

---

## Live-Demo Prompt

```
Lies content.json und erstelle daraus ein spielbares Memory-Spiel
als memory.html. Schönes modernes Design, 4x4 Grid, Karten mit
Flip-Animation, Punktestand und Gewinn-Anzeige.
```

---

## Claude Code: Kurzübersicht

| | |
|---|---|
| **Typ** | Agentic Coding CLI |
| **Hersteller** | Anthropic |
| **Modell** | Claude Sonnet 4.6 (empfohlen) |
| **Plattform** | macOS, Linux, Windows |
| **Pricing** | API Pay-per-use / Claude Pro ($20/Mt.) |
| **Open Source** | Teilweise (SDKs ja, Modelle nein) |

---

## Mitarbeiten

Alle Gruppenmitglieder können direkt Änderungen vorschlagen:
- `content.json` anpassen (andere Themen, mehr Paare)
- `memory.html` weiterentwickeln (neues Design, neue Features)
- Neue Spieltypen hinzufügen (Quiz, Flashcards, ...)

---

*Erstellt mit Claude Code · FHNW 2026*

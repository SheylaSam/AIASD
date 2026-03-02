# Zusammenfassung — AISD Kurs Setup
**FHNW · BSc Business Artificial Intelligence · 4. Semester · 2026**

---

## Was ist das Ziel des Fachs?

Der Kurs "AI-Assisted Software Development" dreht sich um eine zentrale Frage:
**Wie entwickelt man Software heute, mit KI als Co-Entwickler?**

Die Inhalte bauen aufeinander auf:
- SW1: Evolution der Coding-Tools (Code Completion → Agentic Coding)
- SW2: Agile Entwicklung & SDLC im KI-Zeitalter (Waterfall → Scrum → AI-assisted)
- SW3: LLM Auswahl & Deployment
- **Pitch:** Ein Coding-Tool vorstellen (unser Thema: Claude Code)
- **Capstone:** Ein echtes Projekt damit bauen

---

## Was ist ein Capstone-Projekt?

Das Capstone ist das abschliessende Praxisprojekt des Kurses:
- **1–3 Studierende** arbeiten zusammen (wir sind 4)
- Ihr wählt **selbst** einen minimalen Use Case
- Ihr baut eine **Enterprise Full-Stack-Anwendung** mit KI-Unterstützung
- Abgabe: **Source Code + Kurzdokumentation auf GitHub**
- Abschluss: **Präsentation** — Fokus auf Entscheidungsprozesse, Toolauswahl, Learnings

> Wichtig: Bewertet wird nicht wie perfekt die App ist, sondern **wie ihr mit KI-Tools gearbeitet habt und was ihr dabei gelernt habt.**

---

## Unser Coding-Tool: Claude Code

Wir haben **Claude Code** als Coding-Agent gewählt.

| | |
|---|---|
| **Was ist es?** | Agentic Coding CLI von Anthropic — läuft im Terminal & als VS Code Extension |
| **Typ** | Agentic Coding (plant und führt mehrstufige Tasks selbstständig aus) |
| **Modell** | Claude Sonnet 4.6 (empfohlen) |
| **Plattform** | macOS · Linux · Windows |
| **Pricing** | API Pay-per-use (ab ~$5) oder Claude Pro ($20/Mt.) |
| **Open Source** | Nein (Modelle proprietär, SDKs teilweise open source) |

### Warum Claude Code?
- Sheyla nutzt es bereits (seit 2 Wochen bei hazu.swiss)
- Die Gruppe kann es gemeinsam kennenlernen → erfüllt den Kursgedanken
- Perfekt für unser Capstone-Projekt (Python/FastAPI, Tests, Datenbank)

### Installation
Siehe **[SETUP.md](./SETUP.md)** im Repo — Schritt-für-Schritt Anleitung für alle.

---

## Der Pitch (5 Minuten)

Wir präsentieren Claude Code mit allen 7 Pflichtpunkten:
1. Kurzbeschreibung
2. Klassifikation (Agentic Coding ✓, Chat ✓, Code Completion ✗)
3. Kategorie (CLI + VS Code Extension)
4. Model Support (Sonnet / Opus / Haiku)
5. Pricing
6. Open Source
7. **Live Demo**

**Die Präsentation** liegt im Repo: `Claude_Code_Pitch.pptx`

### Live Demo
Wir zeigen Claude Code live: Eine `content.json` mit AISD-Begriffen liegt bereit,
Claude Code generiert daraus in ~20 Sekunden ein spielbares Memory-Spiel.

```bash
cd ~/Desktop/claude-code-demo
claude
# Prompt: "Lies content.json und erstelle daraus ein spielbares Memory-Spiel als memory.html"
open memory.html
```

Das Backup-HTML (`memory.html`) liegt bereits im Repo falls live etwas schiefläuft.

---

## Capstone-Idee: Kollaborative Lernplattform

Wir haben vier Use-Case-Ideen zur Auswahl für die Gruppe:

### Option A — Kollaborative Lernplattform *(Sheylas Favorit)*
> Folien/PDF hochladen → KI erstellt Lernplan + Quizzes → Gruppe lernt gemeinsam daran

- Dokument hochladen (PDF, Folien)
- Claude API generiert: Themenübersicht, Lernplan, Quizzes
- Lernraum erstellen & per Link teilen
- Individueller Fortschritt pro Mitglied

### Option B — AI Job Application Tracker
> Bewerbungen verwalten + KI hilft beim Motivationsschreiben

- Stellenbeschreibung einfügen → KI analysiert und gibt Tipps für CV/Motivationsschreiben
- Status tracken (beworben → Interview → Zusage/Absage)

### Option C — AI Feedback Platform
> Dokument/Präsentation hochladen → strukturiertes KI-Feedback + Peer Review

- Bewertungskriterien selbst definieren
- Versionsverlauf (siehst wie sich dein Dokument verbessert)
- Kommilitoninnen können kommentieren

### Option D — AI Team Project Planner
> Projektbriefing eingeben → KI bricht es in Aufgaben herunter → Team managed gemeinsam

- KI generiert: Aufgabenliste, Zeitplan, Rollenverteilung
- Zwischen Notion (zu manuell) und Jira (zu komplex)

---

## Technischer Stack (Empfehlung für Option A)

```
Frontend (Browser)
      ↓
Backend API (FastAPI / Python)
      ↓              ↓
 Claude API      Datenbank (PostgreSQL)
(Generierung)    (Nutzer, Quizze, Lernpläne)
```

**Mögliche Aufgabenteilung (4 Personen):**
| Person | Bereich |
|---|---|
| Sheyla | Backend API + Claude API Integration |
| Person 2 | Frontend |
| Person 3 | Datenbank + Auth |
| Person 4 | Testing + Deployment + Doku |

---

## Zeitplan (8 Wochen, 4 Sprints)

| Sprint | Thema | Deadline |
|---|---|---|
| Sprint 1 | Setup & Grundstruktur | 16. März |
| Sprint 2 | Upload & KI-Generierung | 30. März |
| Sprint 3 | Lernraum & Gruppen | 13. April |
| Sprint 4 | Polish & Deployment | 27. April |

---

## GitHub Repository

Alles an einem Ort: **https://github.com/SheylaSam/AIASD**

| Was | Wo |
|---|---|
| Pitch-Präsentation | `Claude_Code_Pitch.pptx` |
| Live-Demo Files | `content.json`, `memory.html` |
| Setup-Anleitung | `SETUP.md` |
| Scrum-Board | https://github.com/users/SheylaSam/projects/3 |
| Issues / User Stories | https://github.com/SheylaSam/AIASD/issues |

### Scrum-Board aufgebaut mit:
- **Labels:** user story · backend · frontend · ai-integration · testing · documentation
- **4 Milestones** (= Sprints) mit Deadlines
- **10 vorbereitete Issues** (User Stories & Tasks) — anpassbar sobald wir den Use Case bestätigt haben

---

## Nächste Schritte für die Gruppe

1. **Use Case abstimmen** — Option A, B, C oder D?
2. **Setup** — alle installieren Claude Code gemäss `SETUP.md`
3. **Repo** — Sheyla lädt alle als Collaborators ein (GitHub → Settings → Collaborators)
4. **Sprint 1 starten** — Issues im Board zuweisen und loslegen

---

*Erstellt mit Claude Code · FHNW AISD 2026*

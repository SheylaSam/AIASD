from dataclasses import dataclass, field


@dataclass
class QuizFrage:
    """Eine einzelne Quizfrage mit Antwortoptionen."""
    frage: str
    antworten: list[str]
    richtige_antwort: int  # Index in antworten-Liste

    def __post_init__(self):
        if not self.frage:
            raise ValueError("Frage darf nicht leer sein")
        if len(self.antworten) < 2:
            raise ValueError("Mindestens 2 Antwortoptionen erforderlich")
        if not (0 <= self.richtige_antwort < len(self.antworten)):
            raise ValueError("Richtige Antwort muss ein gültiger Index sein")


@dataclass
class Quiz:
    """Business-Entity: Ein KI-generiertes Quiz zu einem Dokument."""
    title: str
    document_id: int
    fragen: list[QuizFrage] = field(default_factory=list)
    id: int | None = None

    def __post_init__(self):
        if not self.title:
            raise ValueError("Titel darf nicht leer sein")

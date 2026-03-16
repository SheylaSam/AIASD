from abc import ABC, abstractmethod
from app.domain.quiz import Quiz


class QuizRepository(ABC):
    """Port: Abstrakte Schnittstelle für Quiz-Datenzugriff."""

    @abstractmethod
    def save(self, quiz: Quiz) -> Quiz:
        """Quiz speichern."""
        ...

    @abstractmethod
    def find_by_id(self, quiz_id: int) -> Quiz | None:
        """Quiz anhand ID finden."""
        ...

    @abstractmethod
    def find_by_document(self, document_id: int) -> list[Quiz]:
        """Alle Quizzes zu einem Dokument abrufen."""
        ...

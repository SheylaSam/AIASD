from abc import ABC, abstractmethod
from app.domain.lernraum import LernRaum


class LernRaumRepository(ABC):
    """Port: Abstrakte Schnittstelle für LernRaum-Datenzugriff."""

    @abstractmethod
    def save(self, lernraum: LernRaum) -> LernRaum:
        """LernRaum speichern."""
        ...

    @abstractmethod
    def find_by_id(self, lernraum_id: int) -> LernRaum | None:
        """LernRaum anhand ID finden."""
        ...

    @abstractmethod
    def find_by_member(self, user_id: int) -> list[LernRaum]:
        """Alle LernRäume eines Users abrufen."""
        ...

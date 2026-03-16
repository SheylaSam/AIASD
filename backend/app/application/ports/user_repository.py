from abc import ABC, abstractmethod
from app.domain.user import User


class UserRepository(ABC):
    """Port: Abstrakte Schnittstelle für User-Datenzugriff.

    Die Application-Schicht kennt nur dieses Interface,
    nicht die konkrete SQLAlchemy-Implementierung.
    """

    @abstractmethod
    def save(self, user: User) -> User:
        """User speichern (erstellen oder aktualisieren)."""
        ...

    @abstractmethod
    def find_by_id(self, user_id: int) -> User | None:
        """User anhand ID finden."""
        ...

    @abstractmethod
    def find_by_email(self, email: str) -> User | None:
        """User anhand E-Mail finden."""
        ...

    @abstractmethod
    def find_all(self) -> list[User]:
        """Alle User abrufen."""
        ...

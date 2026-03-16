from abc import ABC, abstractmethod
from app.domain.document import Document


class DocumentRepository(ABC):
    """Port: Abstrakte Schnittstelle für Dokument-Datenzugriff."""

    @abstractmethod
    def save(self, document: Document) -> Document:
        """Dokument speichern."""
        ...

    @abstractmethod
    def find_by_id(self, document_id: int) -> Document | None:
        """Dokument anhand ID finden."""
        ...

    @abstractmethod
    def find_by_owner(self, owner_id: int) -> list[Document]:
        """Alle Dokumente eines Users abrufen."""
        ...

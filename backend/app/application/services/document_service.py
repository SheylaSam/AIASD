from app.domain.document import Document
from app.application.ports.document_repository import DocumentRepository


class DocumentService:
    """Use Case: Dokument-Upload und -Verwaltung."""

    def __init__(self, document_repository: DocumentRepository):
        self.document_repository = document_repository

    def upload_document(self, title: str, file_path: str, owner_id: int) -> Document:
        """Neues Dokument hochladen."""
        document = Document(title=title, file_path=file_path, owner_id=owner_id)
        return self.document_repository.save(document)

    def get_document(self, document_id: int) -> Document:
        """Dokument anhand ID abrufen."""
        document = self.document_repository.find_by_id(document_id)
        if not document:
            raise ValueError(f"Dokument nicht gefunden: {document_id}")
        return document

    def get_documents_by_owner(self, owner_id: int) -> list[Document]:
        """Alle Dokumente eines Users abrufen."""
        return self.document_repository.find_by_owner(owner_id)

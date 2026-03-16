from sqlalchemy.orm import Session
from datetime import datetime
from app.domain.document import Document
from app.application.ports.document_repository import DocumentRepository
from app.infrastructure.models import DocumentModel


class SqlAlchemyDocumentRepository(DocumentRepository):
    """Konkrete Implementierung: Dokument-Datenzugriff via SQLAlchemy."""

    def __init__(self, db: Session):
        self.db = db

    def save(self, document: Document) -> Document:
        if document.id is None:
            db_doc = DocumentModel(
                title=document.title,
                file_path=document.file_path,
                owner_id=document.owner_id,
                uploaded_at=datetime.utcnow(),
            )
            self.db.add(db_doc)
        else:
            db_doc = self.db.query(DocumentModel).filter(DocumentModel.id == document.id).first()
            db_doc.title = document.title
            db_doc.file_path = document.file_path
        self.db.commit()
        self.db.refresh(db_doc)
        return self._to_domain(db_doc)

    def find_by_id(self, document_id: int) -> Document | None:
        db_doc = self.db.query(DocumentModel).filter(DocumentModel.id == document_id).first()
        return self._to_domain(db_doc) if db_doc else None

    def find_by_owner(self, owner_id: int) -> list[Document]:
        docs = self.db.query(DocumentModel).filter(DocumentModel.owner_id == owner_id).all()
        return [self._to_domain(d) for d in docs]

    def _to_domain(self, model: DocumentModel) -> Document:
        return Document(
            id=model.id,
            title=model.title,
            file_path=model.file_path,
            owner_id=model.owner_id,
            uploaded_at=model.uploaded_at,
        )

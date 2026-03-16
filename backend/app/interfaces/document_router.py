from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.infrastructure.database import get_db
from app.infrastructure.repositories.document_repository import SqlAlchemyDocumentRepository
from app.application.services.document_service import DocumentService
from app.interfaces.schemas import DocumentCreate, DocumentResponse

router = APIRouter(prefix="/documents", tags=["documents"])


def get_document_service(db: Session = Depends(get_db)) -> DocumentService:
    """Dependency Injection: DocumentService mit SQLAlchemy-Repository aufbauen."""
    repository = SqlAlchemyDocumentRepository(db)
    return DocumentService(repository)


@router.post("/", response_model=DocumentResponse, status_code=201)
def upload_document(data: DocumentCreate, service: DocumentService = Depends(get_document_service)):
    try:
        return service.upload_document(
            title=data.title,
            file_path=data.file_path,
            owner_id=data.owner_id,
        )
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.get("/{document_id}", response_model=DocumentResponse)
def get_document(document_id: int, service: DocumentService = Depends(get_document_service)):
    try:
        return service.get_document(document_id)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))


@router.get("/owner/{owner_id}", response_model=list[DocumentResponse])
def get_documents_by_owner(owner_id: int, service: DocumentService = Depends(get_document_service)):
    return service.get_documents_by_owner(owner_id)

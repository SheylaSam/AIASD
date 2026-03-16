from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.infrastructure.database import get_db
from app.infrastructure.repositories.user_repository import SqlAlchemyUserRepository
from app.application.services.user_service import UserService
from app.interfaces.schemas import UserCreate, UserResponse

router = APIRouter(prefix="/users", tags=["users"])


def get_user_service(db: Session = Depends(get_db)) -> UserService:
    """Dependency Injection: UserService mit SQLAlchemy-Repository aufbauen."""
    repository = SqlAlchemyUserRepository(db)
    return UserService(repository)


@router.post("/", response_model=UserResponse, status_code=201)
def register_user(data: UserCreate, service: UserService = Depends(get_user_service)):
    try:
        return service.register_user(name=data.name, email=data.email)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.get("/", response_model=list[UserResponse])
def list_users(service: UserService = Depends(get_user_service)):
    return service.list_users()


@router.get("/{user_id}", response_model=UserResponse)
def get_user(user_id: int, service: UserService = Depends(get_user_service)):
    try:
        return service.get_user(user_id)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))

from sqlalchemy.orm import Session
from app.domain.user import User
from app.application.ports.user_repository import UserRepository
from app.infrastructure.models import UserModel


class SqlAlchemyUserRepository(UserRepository):
    """Konkrete Implementierung: User-Datenzugriff via SQLAlchemy.

    Übersetzt zwischen Domain-Objekten (User) und DB-Models (UserModel).
    """

    def __init__(self, db: Session):
        self.db = db

    def save(self, user: User) -> User:
        if user.id is None:
            db_user = UserModel(name=user.name, email=user.email)
            self.db.add(db_user)
        else:
            db_user = self.db.query(UserModel).filter(UserModel.id == user.id).first()
            db_user.name = user.name
            db_user.email = user.email
        self.db.commit()
        self.db.refresh(db_user)
        return self._to_domain(db_user)

    def find_by_id(self, user_id: int) -> User | None:
        db_user = self.db.query(UserModel).filter(UserModel.id == user_id).first()
        return self._to_domain(db_user) if db_user else None

    def find_by_email(self, email: str) -> User | None:
        db_user = self.db.query(UserModel).filter(UserModel.email == email).first()
        return self._to_domain(db_user) if db_user else None

    def find_all(self) -> list[User]:
        return [self._to_domain(u) for u in self.db.query(UserModel).all()]

    def _to_domain(self, model: UserModel) -> User:
        """SQLAlchemy-Model → Domain-Objekt."""
        return User(id=model.id, name=model.name, email=model.email)

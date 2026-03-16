from app.domain.user import User
from app.application.ports.user_repository import UserRepository


class UserService:
    """Use Case: User-Verwaltung (registrieren, abrufen)."""

    def __init__(self, user_repository: UserRepository):
        # Dependency Injection: Repository von aussen übergeben
        self.user_repository = user_repository

    def register_user(self, name: str, email: str) -> User:
        """Neuen User registrieren."""
        existing = self.user_repository.find_by_email(email)
        if existing:
            raise ValueError(f"E-Mail bereits registriert: {email}")

        user = User(name=name, email=email)
        return self.user_repository.save(user)

    def get_user(self, user_id: int) -> User:
        """User anhand ID abrufen."""
        user = self.user_repository.find_by_id(user_id)
        if not user:
            raise ValueError(f"User nicht gefunden: {user_id}")
        return user

    def list_users(self) -> list[User]:
        """Alle User abrufen."""
        return self.user_repository.find_all()

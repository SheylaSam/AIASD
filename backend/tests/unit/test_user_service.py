import pytest
from app.domain.user import User
from app.application.services.user_service import UserService
from app.application.ports.user_repository import UserRepository


class FakeUserRepository(UserRepository):
    """Fake-Repository für Unit Tests — kein SQLAlchemy, kein DB."""

    def __init__(self):
        self._users: dict[int, User] = {}
        self._next_id = 1

    def save(self, user: User) -> User:
        user.id = self._next_id
        self._users[self._next_id] = user
        self._next_id += 1
        return user

    def find_by_id(self, user_id: int) -> User | None:
        return self._users.get(user_id)

    def find_by_email(self, email: str) -> User | None:
        return next((u for u in self._users.values() if u.email == email), None)

    def find_all(self) -> list[User]:
        return list(self._users.values())


@pytest.fixture
def service():
    return UserService(FakeUserRepository())


def test_user_registrieren(service):
    user = service.register_user(name="Sheyla", email="sheyla@fhnw.ch")
    assert user.id is not None
    assert user.name == "Sheyla"


def test_doppelte_email_wirft_fehler(service):
    service.register_user(name="Sheyla", email="sheyla@fhnw.ch")
    with pytest.raises(ValueError, match="bereits registriert"):
        service.register_user(name="Andere", email="sheyla@fhnw.ch")


def test_user_abrufen(service):
    erstellt = service.register_user(name="Sheyla", email="sheyla@fhnw.ch")
    gefunden = service.get_user(erstellt.id)
    assert gefunden.email == "sheyla@fhnw.ch"


def test_nicht_vorhandener_user_wirft_fehler(service):
    with pytest.raises(ValueError, match="nicht gefunden"):
        service.get_user(999)


def test_alle_users_auflisten(service):
    service.register_user(name="Sheyla", email="sheyla@fhnw.ch")
    service.register_user(name="Person 2", email="person2@fhnw.ch")
    assert len(service.list_users()) == 2

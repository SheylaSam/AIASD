import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.infrastructure.database import Base
from app.infrastructure.repositories.user_repository import SqlAlchemyUserRepository
from app.domain.user import User


@pytest.fixture
def db():
    """In-Memory SQLite für Integrationstests — keine echte Datei."""
    engine = create_engine("sqlite:///:memory:")
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    yield session
    session.close()


@pytest.fixture
def repo(db):
    return SqlAlchemyUserRepository(db)


def test_user_speichern_und_laden(repo):
    user = User(name="Sheyla", email="sheyla@fhnw.ch")
    gespeichert = repo.save(user)

    assert gespeichert.id is not None
    geladen = repo.find_by_id(gespeichert.id)
    assert geladen.name == "Sheyla"
    assert geladen.email == "sheyla@fhnw.ch"


def test_user_per_email_finden(repo):
    repo.save(User(name="Sheyla", email="sheyla@fhnw.ch"))
    user = repo.find_by_email("sheyla@fhnw.ch")
    assert user is not None
    assert user.name == "Sheyla"


def test_nicht_vorhandener_user_ist_none(repo):
    assert repo.find_by_id(999) is None


def test_alle_users_laden(repo):
    repo.save(User(name="Sheyla", email="sheyla@fhnw.ch"))
    repo.save(User(name="Person 2", email="person2@fhnw.ch"))
    assert len(repo.find_all()) == 2

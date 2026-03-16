import pytest
from app.domain.user import User


def test_user_erstellen():
    user = User(name="Sheyla", email="sheyla@fhnw.ch")
    assert user.name == "Sheyla"
    assert user.email == "sheyla@fhnw.ch"
    assert user.id is None


def test_user_ohne_name_ungueltig():
    with pytest.raises(ValueError, match="Name"):
        User(name="", email="sheyla@fhnw.ch")


def test_user_ohne_at_zeichen_ungueltig():
    with pytest.raises(ValueError, match="E-Mail"):
        User(name="Sheyla", email="keine-email")

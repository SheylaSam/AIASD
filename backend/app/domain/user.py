from dataclasses import dataclass, field


@dataclass
class User:
    """Business-Entity: Ein registrierter Nutzer der Plattform."""
    name: str
    email: str
    id: int | None = None

    def __post_init__(self):
        if not self.name:
            raise ValueError("Name darf nicht leer sein")
        if "@" not in self.email:
            raise ValueError("Ungültige E-Mail-Adresse")

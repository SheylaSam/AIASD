from dataclasses import dataclass
from datetime import datetime


@dataclass
class Document:
    """Business-Entity: Ein hochgeladenes Lernmaterial (PDF, Folien)."""
    title: str
    file_path: str
    owner_id: int
    id: int | None = None
    uploaded_at: datetime | None = None

    def __post_init__(self):
        if not self.title:
            raise ValueError("Titel darf nicht leer sein")
        if not self.file_path:
            raise ValueError("Dateipfad darf nicht leer sein")

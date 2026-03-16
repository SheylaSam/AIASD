from dataclasses import dataclass, field


@dataclass
class LernRaum:
    """Business-Entity: Ein kollaborativer Lernraum für eine Gruppe."""
    name: str
    owner_id: int
    mitglieder_ids: list[int] = field(default_factory=list)
    document_ids: list[int] = field(default_factory=list)
    id: int | None = None

    def __post_init__(self):
        if not self.name:
            raise ValueError("Name darf nicht leer sein")

    def mitglied_hinzufuegen(self, user_id: int) -> None:
        if user_id not in self.mitglieder_ids:
            self.mitglieder_ids.append(user_id)

    def dokument_hinzufuegen(self, document_id: int) -> None:
        if document_id not in self.document_ids:
            self.document_ids.append(document_id)

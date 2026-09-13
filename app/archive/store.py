from .models import ArchiveObject


class ArchiveStore:
    """In-memory storage for GENEZIS Archive Objects."""

    def __init__(self):
        self._objects: dict[str, ArchiveObject] = {}

    def add(self, obj: ArchiveObject) -> None:
        self._objects[obj.id] = obj

    def get(self, object_id: str) -> ArchiveObject | None:
        return self._objects.get(object_id)

    def list_all(self) -> list[ArchiveObject]:
        return list(self._objects.values())

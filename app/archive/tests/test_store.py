from app.archive.models import ArchiveObject
from app.archive.store import ArchiveStore


def test_add_and_get():
    store = ArchiveStore()

    obj = ArchiveObject(
        id="test-1",
        type="note",
        title="Test object",
    )

    store.add(obj)

    assert store.get("test-1") == obj


def test_list_all():
    store = ArchiveStore()

    obj1 = ArchiveObject(
        id="test-1",
        type="note",
        title="First",
    )

    obj2 = ArchiveObject(
        id="test-2",
        type="note",
        title="Second",
    )

    store.add(obj1)
    store.add(obj2)

    assert store.list_all() == [obj1, obj2]

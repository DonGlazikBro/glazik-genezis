from datetime import datetime

from app.archive.models import ArchiveObject


def test_archive_object_creation():
    obj = ArchiveObject(
        id="test-001",
        type="document",
        title="GENEZIS Test Object",
        content="This is a test archive object.",
        source="test",
        tags=["genezis", "test"],
    )

    assert obj.id == "test-001"
    assert obj.type == "document"
    assert obj.title == "GENEZIS Test Object"
    assert obj.content == "This is a test archive object."
    assert obj.source == "test"
    assert obj.tags == ["genezis", "test"]
    assert isinstance(obj.created_at, datetime)
    assert obj.memory_status == "temporary"
    assert obj.memory_priority == 0
    assert obj.relations == []
    assert obj.ai_summary is None
    assert obj.ai_inference is None
    assert obj.history == []

from dataclasses import dataclass, field
from datetime import datetime, timezone
from typing import Any


@dataclass
class ArchiveObject:
    """GENEZIS Archive Object v0.1."""

    id: str
    type: str
    title: str
    content: str = ""

    created_at: datetime = field(
        default_factory=lambda: datetime.now(timezone.utc)
    )

    source: str | None = None
    tags: list[str] = field(default_factory=list)
    context: dict[str, Any] = field(default_factory=dict)

    memory_status: str = "temporary"
    memory_priority: int = 0

    relations: list[str] = field(default_factory=list)

    ai_summary: str | None = None
    ai_inference: str | None = None

    history: list[dict[str, Any]] = field(default_factory=list)

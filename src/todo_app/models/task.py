"""Task data model for the Todo Console App."""

from dataclasses import dataclass
from datetime import datetime
from typing import Optional


@dataclass
class Task:
    """Represents a single todo item that can be managed by the user."""

    id: int
    title: str
    description: str
    completed: bool = False
    created_at: datetime = None

    def __post_init__(self):
        """Initialize the created_at field if not provided."""
        if self.created_at is None:
            self.created_at = datetime.now()

    def validate(self) -> None:
        """Validate the task fields according to business rules."""
        # Title must not be empty or only whitespace
        if not self.title or not self.title.strip():
            raise ValueError("Title must not be empty or only whitespace")

        # Title must be between 1 and 100 characters
        if len(self.title) > 100:
            raise ValueError("Title must be between 1 and 100 characters")

        # Description can be empty but if provided, must be up to 500 characters
        if self.description and len(self.description) > 500:
            raise ValueError("Description must be 500 characters or less")

        # ID must be a positive integer
        if self.id <= 0:
            raise ValueError("ID must be a positive integer")

    def to_dict(self) -> dict:
        """Convert the task to a dictionary representation."""
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "completed": self.completed,
            "created_at": self.created_at.isoformat()
        }

    @classmethod
    def from_dict(cls, data: dict) -> 'Task':
        """Create a Task instance from a dictionary."""
        return cls(
            id=data["id"],
            title=data["title"],
            description=data.get("description", ""),
            completed=data.get("completed", False),
            created_at=datetime.fromisoformat(data["created_at"]) if data.get("created_at") else datetime.now()
        )
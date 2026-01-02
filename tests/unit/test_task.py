"""Unit tests for the Task model."""

import pytest
from datetime import datetime
from src.todo_app.models.task import Task


class TestTask:
    """Test cases for the Task model."""

    def test_task_creation_valid(self):
        """Test creating a valid task."""
        task = Task(id=1, title="Test Task", description="Test Description")

        assert task.id == 1
        assert task.title == "Test Task"
        assert task.description == "Test Description"
        assert task.completed is False
        assert isinstance(task.created_at, datetime)

    def test_task_creation_defaults(self):
        """Test creating a task with default values."""
        task = Task(id=1, title="Test Task", description="")

        assert task.id == 1
        assert task.title == "Test Task"
        assert task.description == ""
        assert task.completed is False

    def test_task_validation_valid_title(self):
        """Test validation with valid title."""
        task = Task(id=1, title="Valid Title", description="Description")
        task.validate()  # Should not raise an exception

    def test_task_validation_empty_title(self):
        """Test validation with empty title."""
        task = Task(id=1, title="", description="Description")

        with pytest.raises(ValueError, match="Title must not be empty or only whitespace"):
            task.validate()

    def test_task_validation_whitespace_only_title(self):
        """Test validation with whitespace-only title."""
        task = Task(id=1, title="   ", description="Description")

        with pytest.raises(ValueError, match="Title must not be empty or only whitespace"):
            task.validate()

    def test_task_validation_long_title(self):
        """Test validation with title exceeding 100 characters."""
        long_title = "A" * 101
        task = Task(id=1, title=long_title, description="Description")

        with pytest.raises(ValueError, match="Title must be between 1 and 100 characters"):
            task.validate()

    def test_task_validation_valid_long_description(self):
        """Test validation with description up to 500 characters."""
        long_description = "A" * 500
        task = Task(id=1, title="Title", description=long_description)
        task.validate()  # Should not raise an exception

    def test_task_validation_too_long_description(self):
        """Test validation with description exceeding 500 characters."""
        long_description = "A" * 501
        task = Task(id=1, title="Title", description=long_description)

        with pytest.raises(ValueError, match="Description must be 500 characters or less"):
            task.validate()

    def test_task_validation_negative_id(self):
        """Test validation with negative ID."""
        task = Task(id=-1, title="Title", description="Description")

        with pytest.raises(ValueError, match="ID must be a positive integer"):
            task.validate()

    def test_task_validation_zero_id(self):
        """Test validation with zero ID."""
        task = Task(id=0, title="Title", description="Description")

        with pytest.raises(ValueError, match="ID must be a positive integer"):
            task.validate()

    def test_task_to_dict(self):
        """Test converting task to dictionary."""
        task = Task(id=1, title="Test Task", description="Test Description", completed=True)
        task_dict = task.to_dict()

        assert task_dict["id"] == 1
        assert task_dict["title"] == "Test Task"
        assert task_dict["description"] == "Test Description"
        assert task_dict["completed"] is True
        assert "created_at" in task_dict

    def test_task_from_dict(self):
        """Test creating task from dictionary."""
        task_data = {
            "id": 1,
            "title": "Test Task",
            "description": "Test Description",
            "completed": True,
            "created_at": datetime.now().isoformat()
        }
        task = Task.from_dict(task_data)

        assert task.id == 1
        assert task.title == "Test Task"
        assert task.description == "Test Description"
        assert task.completed is True
        assert isinstance(task.created_at, datetime)
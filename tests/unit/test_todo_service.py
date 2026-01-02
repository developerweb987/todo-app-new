"""Unit tests for the TodoService."""

import pytest
from src.todo_app.services.todo_service import TodoService
from src.todo_app.models.task import Task


class TestTodoService:
    """Test cases for the TodoService."""

    def test_add_task_success(self):
        """Test successfully adding a task."""
        service = TodoService()
        task = service.add_task("Test Title", "Test Description")

        assert task.id == 1
        assert task.title == "Test Title"
        assert task.description == "Test Description"
        assert task.completed is False
        assert len(service.get_all_tasks()) == 1

    def test_add_task_default_description(self):
        """Test adding a task with default empty description."""
        service = TodoService()
        task = service.add_task("Test Title")

        assert task.id == 1
        assert task.title == "Test Title"
        assert task.description == ""
        assert task.completed is False

    def test_add_task_validation_error(self):
        """Test adding a task with invalid title raises ValueError."""
        service = TodoService()

        with pytest.raises(ValueError, match="Title must not be empty or only whitespace"):
            service.add_task("")

    def test_add_task_duplicate_title(self):
        """Test adding a task with duplicate title raises ValueError."""
        service = TodoService()
        service.add_task("Duplicate Title", "First task")

        with pytest.raises(ValueError, match="A task with title 'Duplicate Title' already exists"):
            service.add_task("Duplicate Title", "Second task")

    def test_add_task_duplicate_title_different_case(self):
        """Test adding a task with same title but different case is allowed."""
        service = TodoService()
        service.add_task("Duplicate Title", "First task")
        task = service.add_task("duplicate title", "Second task")

        assert len(service.get_all_tasks()) == 2
        assert task.id == 2

    def test_add_task_duplicate_title_completed_task(self):
        """Test adding a task with same title as completed task is allowed."""
        service = TodoService()
        task1 = service.add_task("Duplicate Title", "First task")
        service.mark_complete(task1.id)  # Mark the first task as completed

        # Adding a new task with the same title should be allowed
        task2 = service.add_task("Duplicate Title", "Second task")

        assert len(service.get_all_tasks()) == 2
        assert task2.id == 2

    def test_get_task_found(self):
        """Test getting an existing task."""
        service = TodoService()
        added_task = service.add_task("Test Title", "Test Description")

        retrieved_task = service.get_task(added_task.id)

        assert retrieved_task is not None
        assert retrieved_task.id == added_task.id
        assert retrieved_task.title == added_task.title
        assert retrieved_task.description == added_task.description

    def test_get_task_not_found(self):
        """Test getting a non-existing task returns None."""
        service = TodoService()

        retrieved_task = service.get_task(999)

        assert retrieved_task is None

    def test_get_all_tasks(self):
        """Test getting all tasks."""
        service = TodoService()
        task1 = service.add_task("Task 1", "Description 1")
        task2 = service.add_task("Task 2", "Description 2")

        all_tasks = service.get_all_tasks()

        assert len(all_tasks) == 2
        assert all_tasks[0].id == task1.id
        assert all_tasks[1].id == task2.id

    def test_update_task_success(self):
        """Test successfully updating a task."""
        service = TodoService()
        original_task = service.add_task("Original Title", "Original Description")

        updated_task = service.update_task(original_task.id, "New Title", "New Description")

        assert updated_task is not None
        assert updated_task.id == original_task.id
        assert updated_task.title == "New Title"
        assert updated_task.description == "New Description"

    def test_update_task_partial(self):
        """Test updating only title or description."""
        service = TodoService()
        original_task = service.add_task("Original Title", "Original Description")

        # Update only the title
        updated_task = service.update_task(original_task.id, title="New Title")

        assert updated_task is not None
        assert updated_task.id == original_task.id
        assert updated_task.title == "New Title"
        assert updated_task.description == "Original Description"  # Should remain unchanged

        # Update only the description
        updated_task = service.update_task(original_task.id, description="New Description")

        assert updated_task is not None
        assert updated_task.id == original_task.id
        assert updated_task.title == "New Title"  # Should remain unchanged
        assert updated_task.description == "New Description"

    def test_update_task_not_found(self):
        """Test updating a non-existing task returns None."""
        service = TodoService()

        result = service.update_task(999, "New Title")

        assert result is None

    def test_update_task_validation_error(self):
        """Test updating a task with invalid title raises ValueError."""
        service = TodoService()
        original_task = service.add_task("Original Title", "Original Description")

        with pytest.raises(ValueError, match="Title must not be empty or only whitespace"):
            service.update_task(original_task.id, "")

    def test_delete_task_success(self):
        """Test successfully deleting a task."""
        service = TodoService()
        task = service.add_task("Test Title", "Test Description")

        result = service.delete_task(task.id)

        assert result is True
        assert service.get_task(task.id) is None
        assert len(service.get_all_tasks()) == 0

    def test_delete_task_not_found(self):
        """Test deleting a non-existing task returns False."""
        service = TodoService()

        result = service.delete_task(999)

        assert result is False

    def test_mark_complete_success(self):
        """Test successfully marking a task as complete."""
        service = TodoService()
        task = service.add_task("Test Title", "Test Description")

        result = service.mark_complete(task.id)

        assert result is True
        assert service.get_task(task.id).completed is True

    def test_mark_complete_not_found(self):
        """Test marking a non-existing task as complete returns False."""
        service = TodoService()

        result = service.mark_complete(999)

        assert result is False

    def test_mark_incomplete_success(self):
        """Test successfully marking a task as incomplete."""
        service = TodoService()
        task = service.add_task("Test Title", "Test Description")
        service.mark_complete(task.id)  # First mark as complete

        result = service.mark_incomplete(task.id)

        assert result is True
        assert service.get_task(task.id).completed is False

    def test_mark_incomplete_not_found(self):
        """Test marking a non-existing task as incomplete returns False."""
        service = TodoService()

        result = service.mark_incomplete(999)

        assert result is False

    def test_get_completed_tasks(self):
        """Test getting completed tasks."""
        service = TodoService()
        task1 = service.add_task("Task 1", "Description 1")
        task2 = service.add_task("Task 2", "Description 2")
        service.mark_complete(task1.id)  # Mark first task as complete

        completed_tasks = service.get_completed_tasks()

        assert len(completed_tasks) == 1
        assert completed_tasks[0].id == task1.id
        assert completed_tasks[0].completed is True

    def test_get_pending_tasks(self):
        """Test getting pending tasks."""
        service = TodoService()
        task1 = service.add_task("Task 1", "Description 1")
        task2 = service.add_task("Task 2", "Description 2")
        service.mark_complete(task1.id)  # Mark first task as complete

        pending_tasks = service.get_pending_tasks()

        assert len(pending_tasks) == 1
        assert pending_tasks[0].id == task2.id
        assert pending_tasks[0].completed is False

    def test_task_id_generation(self):
        """Test that task IDs are generated sequentially."""
        service = TodoService()
        task1 = service.add_task("Task 1", "Description 1")
        task2 = service.add_task("Task 2", "Description 2")
        task3 = service.add_task("Task 3", "Description 3")

        assert task1.id == 1
        assert task2.id == 2
        assert task3.id == 3
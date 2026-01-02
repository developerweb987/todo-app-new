"""Core business logic for the Todo Console App."""

from typing import List, Optional
import logging
from todo_app.models.task import Task


# Configure logging for the service
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class TodoService:
    """Service for managing tasks in memory."""

    def __init__(self):
        """Initialize the service with an empty list of tasks."""
        self._tasks: List[Task] = []
        self._next_id = 1

    def add_task(self, title: str, description: str = "") -> Task:
        """Creates new task with unique ID."""
        logger.info(f"Adding new task: title='{title}', description='{description}'")

        # Validate inputs before creating task
        temp_task = Task(id=self._next_id, title=title, description=description)
        temp_task.validate()

        # Check for duplicate title (optional validation)
        for task in self._tasks:
            if task.title == title and not task.completed:
                logger.warning(f"Duplicate task title detected: '{title}'")
                raise ValueError(f"A task with title '{title}' already exists")

        task = Task(id=self._next_id, title=title, description=description)
        self._tasks.append(task)
        task_id = self._next_id
        self._next_id += 1

        logger.info(f"Task added successfully with ID: {task_id}")
        return task

    def get_task(self, task_id: int) -> Optional[Task]:
        """Retrieves specific task by ID."""
        logger.debug(f"Retrieving task with ID: {task_id}")
        for task in self._tasks:
            if task.id == task_id:
                logger.debug(f"Task found: ID {task_id}")
                return task
        logger.warning(f"Task not found: ID {task_id}")
        return None

    def get_all_tasks(self) -> List[Task]:
        """Returns all tasks in the list."""
        logger.debug(f"Retrieving all tasks ({len(self._tasks)} total)")
        return self._tasks.copy()

    def update_task(self, task_id: int, title: str = None, description: str = None) -> Optional[Task]:
        """Modifies existing task."""
        logger.info(f"Updating task with ID: {task_id}")
        task = self.get_task(task_id)
        if not task:
            logger.error(f"Cannot update task: ID {task_id} not found")
            return None

        # Use existing values if new values are not provided
        new_title = title if title is not None else task.title
        new_description = description if description is not None else task.description

        # Validate the updated values
        temp_task = Task(id=task.id, title=new_title, description=new_description)
        temp_task.validate()

        # Update the task
        old_title = task.title
        task.title = new_title
        task.description = new_description

        logger.info(f"Task updated: ID {task_id}, '{old_title}' -> '{new_title}'")
        return task

    def delete_task(self, task_id: int) -> bool:
        """Removes task from list."""
        logger.info(f"Deleting task with ID: {task_id}")
        task = self.get_task(task_id)
        if not task:
            logger.error(f"Cannot delete task: ID {task_id} not found")
            return False

        self._tasks.remove(task)
        logger.info(f"Task deleted: ID {task_id}")
        return True

    def mark_complete(self, task_id: int) -> bool:
        """Sets task status to completed."""
        logger.info(f"Marking task as complete: ID {task_id}")
        task = self.get_task(task_id)
        if not task:
            logger.error(f"Cannot mark task complete: ID {task_id} not found")
            return False

        if task.completed:
            logger.warning(f"Task already marked as complete: ID {task_id}")
        else:
            task.completed = True
            logger.info(f"Task marked as complete: ID {task_id}")
        return True

    def mark_incomplete(self, task_id: int) -> bool:
        """Sets task status to incomplete."""
        logger.info(f"Marking task as incomplete: ID {task_id}")
        task = self.get_task(task_id)
        if not task:
            logger.error(f"Cannot mark task incomplete: ID {task_id} not found")
            return False

        if not task.completed:
            logger.warning(f"Task already marked as incomplete: ID {task_id}")
        else:
            task.completed = False
            logger.info(f"Task marked as incomplete: ID {task_id}")
        return True

    def get_completed_tasks(self) -> List[Task]:
        """Returns only completed tasks."""
        completed_tasks = [task for task in self._tasks if task.completed]
        logger.debug(f"Retrieved {len(completed_tasks)} completed tasks")
        return completed_tasks

    def get_pending_tasks(self) -> List[Task]:
        """Returns only pending tasks."""
        pending_tasks = [task for task in self._tasks if not task.completed]
        logger.debug(f"Retrieved {len(pending_tasks)} pending tasks")
        return pending_tasks
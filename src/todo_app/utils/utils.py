"""Utility functions for the Todo Console App."""

from typing import List
from todo_app.models.task import Task


def format_task_list(tasks: List[Task]) -> str:
    """Format a list of tasks for display in the console.

    Args:
        tasks: List of Task objects to format

    Returns:
        Formatted string representation of the tasks
    """
    if not tasks:
        return "No tasks found."

    lines = []
    for task in tasks:
        status = "✓" if task.completed else "○"
        lines.append(f"{status} [{task.id}] {task.title} - {task.description}")

    return "\n".join(lines)


def get_task_summary(tasks: List[Task]) -> str:
    """Get a summary of tasks (total, completed, pending).

    Args:
        tasks: List of Task objects

    Returns:
        Summary string with counts
    """
    total = len(tasks)
    completed = len([task for task in tasks if task.completed])
    pending = total - completed

    return f"Total: {total}, Completed: {completed}, Pending: {pending}"


def validate_task_id(task_id: str) -> bool:
    """Validate that a task ID string is a positive integer.

    Args:
        task_id: String representation of task ID

    Returns:
        True if valid, False otherwise
    """
    try:
        id_num = int(task_id)
        return id_num > 0
    except ValueError:
        return False
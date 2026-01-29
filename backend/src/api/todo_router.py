from fastapi import APIRouter, Depends, HTTPException, status
from sqlmodel import Session
from typing import List
from ..database.database import get_session
from ..models.todo_task import TodoTask, TodoTaskPublic, TodoTaskUpdate
from ..middleware.auth_middleware import get_current_user
from ..services.todo_service import TodoService

router = APIRouter(prefix="/api/{user_id}", tags=["tasks"])

@router.get("/tasks")
def get_tasks(
    user_id: str,
    current_user_id: str = Depends(get_current_user),
    session: Session = Depends(get_session)
):
    """
    Retrieve all tasks for the specified user
    """
    # Verify that the authenticated user is accessing their own data
    if user_id != current_user_id:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Access denied: You can only access your own tasks"
        )

    tasks = TodoService.get_user_todos(session, user_id)
    return tasks  # Return raw data for successful response

@router.post("/tasks")
def create_task(
    user_id: str,
    task_data: TodoTaskUpdate,
    current_user_id: str = Depends(get_current_user),
    session: Session = Depends(get_session)
):
    """
    Create a new task for the specified user
    """
    # Verify that the authenticated user is creating tasks for themselves
    if user_id != current_user_id:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Access denied: You can only create tasks for yourself"
        )

    # Validate title is provided
    if not task_data.title or len(task_data.title.strip()) == 0:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Title is required"
        )

    # Create new task using service
    db_task = TodoService.create_todo(session, user_id, task_data.title, task_data.description)
    return db_task  # Return raw data for successful response

@router.get("/tasks/{task_id}")
def get_task(
    user_id: str,
    task_id: str,
    current_user_id: str = Depends(get_current_user),
    session: Session = Depends(get_session)
):
    """
    Retrieve a specific task for the specified user
    """
    # Verify that the authenticated user is accessing their own data
    if user_id != current_user_id:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Access denied: You can only access your own tasks"
        )

    task = TodoService.get_todo_by_id(session, task_id, user_id)

    if not task:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Task not found or access denied"
        )

    return task  # Return raw data for successful response

@router.put("/tasks/{task_id}")
def update_task(
    user_id: str,
    task_id: str,
    task_update: TodoTaskUpdate,
    current_user_id: str = Depends(get_current_user),
    session: Session = Depends(get_session)
):
    """
    Update a specific task for the specified user
    """
    # Verify that the authenticated user is updating their own task
    if user_id != current_user_id:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Access denied: You can only update your own tasks"
        )

    # Use the TodoService to update the task
    updated_task = TodoService.update_todo(
        session,
        task_id,
        user_id,
        task_update.title,
        task_update.description,
        task_update.is_completed
    )

    return updated_task  # Return raw data for successful response

@router.patch("/tasks/{task_id}/complete")
def toggle_task_complete(
    user_id: str,
    task_id: str,
    completion_data: TodoTaskUpdate,
    current_user_id: str = Depends(get_current_user),
    session: Session = Depends(get_session)
):
    """
    Toggle completion status of a task
    """
    # Verify that the authenticated user is updating their own task
    if user_id != current_user_id:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Access denied: You can only update your own tasks"
        )

    # Validate that is_completed is provided
    if completion_data.is_completed is None:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="is_completed field is required"
        )

    # Use the TodoService to toggle completion status
    updated_task = TodoService.toggle_todo_completion(session, task_id, user_id, completion_data.is_completed)

    return updated_task  # Return raw data for successful response

@router.delete("/tasks/{task_id}")
def delete_task(
    user_id: str,
    task_id: str,
    current_user_id: str = Depends(get_current_user),
    session: Session = Depends(get_session)
):
    """
    Delete a specific task for the specified user
    """
    # Verify that the authenticated user is deleting their own task
    if user_id != current_user_id:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Access denied: You can only delete your own tasks"
        )

    success = TodoService.delete_todo(session, task_id, user_id)

    if not success:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Task not found or access denied"
        )

    return {"message": "Task deleted successfully"}  # Standard response for delete operations
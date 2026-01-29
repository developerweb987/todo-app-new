from sqlmodel import Session, select
from typing import List, Optional
from datetime import datetime
from ..models.todo_task import TodoTask, TodoTaskUpdate
from ..models.user import User
from fastapi import HTTPException, status
from ..middleware.auth_middleware import verify_user_owns_resource

class TodoService:
    @staticmethod
    def get_user_todos(session: Session, user_id: str) -> List[TodoTask]:
        """
        Retrieve all todos for a specific user
        """
        statement = select(TodoTask).where(TodoTask.user_id == user_id)
        return session.exec(statement).all()

    @staticmethod
    def get_todo_by_id(session: Session, todo_id: str, user_id: str) -> Optional[TodoTask]:
        """
        Retrieve a specific todo by ID for the user
        """
        statement = select(TodoTask).where(
            TodoTask.id == todo_id,
            TodoTask.user_id == user_id
        )
        todo = session.exec(statement).first()

        if todo:
            # Verify that the user owns the resource
            verify_user_owns_resource(user_id, todo.user_id)

        return todo

    @staticmethod
    def create_todo(session: Session, user_id: str, title: str, description: str = None) -> TodoTask:
        """
        Create a new todo for the user
        """
        if not title or len(title.strip()) == 0:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Title is required"
            )

        db_todo = TodoTask(
            title=title,
            description=description,
            is_completed=False,
            user_id=user_id
        )
        session.add(db_todo)
        session.commit()
        session.refresh(db_todo)
        return db_todo

    @staticmethod
    def update_todo(
        session: Session,
        todo_id: str,
        user_id: str,
        title: str = None,
        description: str = None,
        is_completed: bool = None
    ) -> TodoTask:
        """
        Update a specific todo for the user
        """
        statement = select(TodoTask).where(
            TodoTask.id == todo_id
        )
        todo = session.exec(statement).first()

        if not todo:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Todo not found"
            )

        # Verify that the user owns the resource
        verify_user_owns_resource(user_id, todo.user_id)

        # Update fields if provided
        if title is not None:
            todo.title = title
        if description is not None:
            todo.description = description
        if is_completed is not None:
            todo.is_completed = is_completed

        todo.updated_at = datetime.utcnow()
        session.add(todo)
        session.commit()
        session.refresh(todo)
        return todo

    @staticmethod
    def toggle_todo_completion(session: Session, todo_id: str, user_id: str, is_completed: bool) -> TodoTask:
        """
        Toggle completion status of a todo
        """
        statement = select(TodoTask).where(
            TodoTask.id == todo_id
        )
        todo = session.exec(statement).first()

        if not todo:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Todo not found"
            )

        # Verify that the user owns the resource
        verify_user_owns_resource(user_id, todo.user_id)

        todo.is_completed = is_completed
        todo.updated_at = datetime.utcnow()
        session.add(todo)
        session.commit()
        session.refresh(todo)
        return todo

    @staticmethod
    def delete_todo(session: Session, todo_id: str, user_id: str) -> bool:
        """
        Delete a specific todo for the user
        """
        statement = select(TodoTask).where(
            TodoTask.id == todo_id
        )
        todo = session.exec(statement).first()

        if not todo:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Todo not found"
            )

        # Verify that the user owns the resource
        verify_user_owns_resource(user_id, todo.user_id)

        session.delete(todo)
        session.commit()
        return True
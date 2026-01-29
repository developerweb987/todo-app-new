from sqlmodel import SQLModel, Field
from datetime import datetime
from typing import Optional
import uuid

class TodoTaskBase(SQLModel):
    title: str
    description: Optional[str] = None
    is_completed: bool = Field(default=False)
    user_id: str = Field(foreign_key="user.id")

class TodoTask(TodoTaskBase, table=True):
    id: str = Field(default_factory=lambda: str(uuid.uuid4()), primary_key=True)
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

class TodoTaskPublic(TodoTaskBase):
    id: str
    created_at: datetime
    updated_at: datetime

class TodoTaskUpdate(SQLModel):
    title: Optional[str] = None
    description: Optional[str] = None
    is_completed: Optional[bool] = None
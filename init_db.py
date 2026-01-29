import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), 'backend'))

from sqlmodel import SQLModel
from backend.src.database.database import engine
from backend.src.models.user import User
from backend.src.models.todo_task import TodoTask

def create_db_and_tables():
    SQLModel.metadata.create_all(engine)

if __name__ == "__main__":
    create_db_and_tables()
    print("Database tables created successfully!")
from sqlmodel import create_engine, Session
from typing import Generator
import os
from dotenv import load_dotenv

load_dotenv()

# Database URL from environment variable
DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./todo_app_local.db")  # Use local SQLite for development

# Create engine with connection pooling settings
# Use different settings for SQLite vs PostgreSQL
if DATABASE_URL.startswith("sqlite"):
    engine = create_engine(
        DATABASE_URL,
        echo=False,  # Set to False in production
        connect_args={"check_same_thread": False}  # Required for SQLite with threading
    )
else:
    engine = create_engine(
        DATABASE_URL,
        pool_size=5,
        max_overflow=10,
        pool_pre_ping=True,
        echo=False  # Set to False in production
    )

def get_session() -> Generator[Session, None, None]:
    """Dependency to get database session"""
    try:
        with Session(engine) as session:
            yield session
    except Exception as e:
        print(f"Database session error: {str(e)}")
        raise
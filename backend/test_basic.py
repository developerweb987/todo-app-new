"""
Basic test to verify the backend components are working correctly.
"""
from src.models.user import User, UserPublic
from src.models.todo_task import TodoTask, TodoTaskPublic, TodoTaskUpdate
from src.services.auth_service import AuthService
from src.services.todo_service import TodoService
from src.database.database import get_session, engine
from sqlmodel import Session, select

def test_models():
    """Test that models can be instantiated."""
    print("Testing models...")

    # Test User model
    user = User(
        email="test@example.com",
        hashed_password="hashed_password_here"
    )
    assert user.email == "test@example.com"
    print("✓ User model works")

    # Test TodoTask model
    todo = TodoTask(
        title="Test task",
        description="Test description",
        user_id="some_user_id"
    )
    assert todo.title == "Test task"
    print("✓ TodoTask model works")

def test_services():
    """Test that services are available."""
    print("\nTesting services...")

    # Test AuthService exists and has required methods
    assert hasattr(AuthService, 'register_user')
    assert hasattr(AuthService, 'authenticate_user')
    assert hasattr(AuthService, 'generate_auth_token')
    print("✓ AuthService methods available")

    # Test TodoService exists and has required methods
    assert hasattr(TodoService, 'get_user_todos')
    assert hasattr(TodoService, 'create_todo')
    assert hasattr(TodoService, 'update_todo')
    assert hasattr(TodoService, 'delete_todo')
    print("✓ TodoService methods available")

def test_database_connection():
    """Test that database connection works."""
    print("\nTesting database connection...")

    try:
        # Try to get a session
        session_gen = get_session()
        session = next(session_gen)

        # Test a simple query (won't find anything but shouldn't error)
        result = session.exec(select(User).limit(1)).first()

        print("✓ Database connection works")
        return True
    except Exception as e:
        print(f"✗ Database connection failed: {e}")
        return False
    finally:
        # Close the session
        session.close()

if __name__ == "__main__":
    print("Running basic backend tests...\n")

    test_models()
    test_services()
    db_ok = test_database_connection()

    if db_ok:
        print("\n✓ All basic tests passed!")
    else:
        print("\n✗ Some tests failed!")
        exit(1)
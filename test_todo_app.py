"""Simple test to verify the todo app modules import correctly."""

import sys
import os

# Add the src directory to the Python path so we can import the todo_app modules
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

def test_imports():
    """Test that all modules can be imported without errors."""
    try:
        from todo_app.models.task import Task
        print("SUCCESS: Task model imported successfully")

        from todo_app.services.todo_service import TodoService
        print("SUCCESS: TodoService imported successfully")

        from todo_app.utils.utils import format_task_list, get_task_summary, validate_task_id
        print("SUCCESS: Utils module imported successfully")

        from todo_app.main import display_menu, add_task, view_all_tasks
        print("SUCCESS: Main module imported successfully")

        print("\nSUCCESS: All imports successful!")
        return True
    except ImportError as e:
        print(f"ERROR: Import error: {e}")
        return False
    except Exception as e:
        print(f"ERROR: Other error: {e}")
        import traceback
        traceback.print_exc()
        return False

def test_basic_functionality():
    """Test basic functionality of the todo app."""
    try:
        from todo_app.services.todo_service import TodoService
        from todo_app.models.task import Task

        # Create a service instance
        service = TodoService()
        print("SUCCESS: TodoService instantiated successfully")

        # Test adding a task
        task = service.add_task("Test Task", "This is a test task")
        print(f"SUCCESS: Task added successfully: ID {task.id}, Title '{task.title}'")

        # Test getting all tasks
        tasks = service.get_all_tasks()
        print(f"SUCCESS: Retrieved {len(tasks)} task(s)")

        # Test marking task as complete
        success = service.mark_complete(task.id)
        print(f"SUCCESS: Marked task as complete: {success}")

        # Test updating task
        updated_task = service.update_task(task.id, "Updated Test Task", "Updated description")
        print(f"SUCCESS: Task updated successfully: Title '{updated_task.title}'")

        # Test deleting task
        delete_success = service.delete_task(task.id)
        print(f"SUCCESS: Task deleted successfully: {delete_success}")

        print("\nSUCCESS: All basic functionality tests passed!")
        return True
    except Exception as e:
        print(f"ERROR: Basic functionality test error: {e}")
        import traceback
        traceback.print_exc()
        return False

if __name__ == "__main__":
    print("Testing Todo App Imports and Basic Functionality...\n")

    print("1. Testing imports:")
    imports_ok = test_imports()

    print("\n2. Testing basic functionality:")
    functionality_ok = test_basic_functionality()

    print(f"\nOverall result: {'SUCCESS: All tests passed!' if imports_ok and functionality_ok else 'ERROR: Some tests failed'}")
"""Main entry point for the Todo Console App."""

from todo_app.services.todo_service import TodoService
from todo_app.utils.utils import format_task_list, get_task_summary, validate_task_id


def display_menu():
    """Display the main menu options."""
    print("\n" + "="*40)
    print("TODO CONSOLE APP")
    print("="*40)
    print("1. Add Task")
    print("2. View All Tasks")
    print("3. Update Task")
    print("4. Delete Task")
    print("5. Mark Task Complete")
    print("6. Mark Task Incomplete")
    print("7. View Completed Tasks")
    print("8. View Pending Tasks")
    print("0. Exit")
    print("="*40)


def get_user_input(prompt: str) -> str:
    """Get input from the user with a prompt.

    Args:
        prompt: The prompt to display to the user

    Returns:
        The user's input as a string
    """
    return input(prompt).strip()


def add_task(service: TodoService):
    """Handle adding a new task."""
    print("\n--- Add New Task ---")
    title = get_user_input("Enter task title: ")

    if not title:
        print("Error: Title cannot be empty!")
        return

    description = get_user_input("Enter task description (optional, press Enter to skip): ")

    try:
        task = service.add_task(title, description)
        print(f"Task added successfully with ID: {task.id}")
    except ValueError as e:
        print(f"Error adding task: {e}")


def view_all_tasks(service: TodoService):
    """Handle viewing all tasks."""
    print("\n--- All Tasks ---")
    tasks = service.get_all_tasks()
    summary = get_task_summary(tasks)
    print(f"\n{summary}")
    print("\n" + format_task_list(tasks))


def update_task(service: TodoService):
    """Handle updating an existing task."""
    print("\n--- Update Task ---")
    task_id_str = get_user_input("Enter task ID to update: ")

    if not validate_task_id(task_id_str):
        print("Error: Invalid task ID. Please enter a positive integer.")
        return

    task_id = int(task_id_str)
    task = service.get_task(task_id)

    if not task:
        print(f"Error: Task with ID {task_id} not found.")
        return

    print(f"Current task: {task.title} - {task.description}")

    new_title = get_user_input(f"Enter new title (current: '{task.title}', press Enter to keep current): ")
    new_description = get_user_input(f"Enter new description (current: '{task.description}', press Enter to keep current): ")

    # Use None for values that should not be updated
    title_to_update = new_title if new_title else None
    description_to_update = new_description if new_description else None

    try:
        updated_task = service.update_task(task_id, title_to_update, description_to_update)
        if updated_task:
            print("Task updated successfully!")
        else:
            print("Failed to update task.")
    except ValueError as e:
        print(f"Error updating task: {e}")


def delete_task(service: TodoService):
    """Handle deleting a task."""
    print("\n--- Delete Task ---")
    task_id_str = get_user_input("Enter task ID to delete: ")

    if not validate_task_id(task_id_str):
        print("Error: Invalid task ID. Please enter a positive integer.")
        return

    task_id = int(task_id_str)
    success = service.delete_task(task_id)

    if success:
        print(f"Task with ID {task_id} deleted successfully!")
    else:
        print(f"Error: Task with ID {task_id} not found.")


def mark_task_complete(service: TodoService):
    """Handle marking a task as complete."""
    print("\n--- Mark Task Complete ---")
    task_id_str = get_user_input("Enter task ID to mark complete: ")

    if not validate_task_id(task_id_str):
        print("Error: Invalid task ID. Please enter a positive integer.")
        return

    task_id = int(task_id_str)
    success = service.mark_complete(task_id)

    if success:
        print(f"Task with ID {task_id} marked as complete!")
    else:
        print(f"Error: Task with ID {task_id} not found.")


def mark_task_incomplete(service: TodoService):
    """Handle marking a task as incomplete."""
    print("\n--- Mark Task Incomplete ---")
    task_id_str = get_user_input("Enter task ID to mark incomplete: ")

    if not validate_task_id(task_id_str):
        print("Error: Invalid task ID. Please enter a positive integer.")
        return

    task_id = int(task_id_str)
    success = service.mark_incomplete(task_id)

    if success:
        print(f"Task with ID {task_id} marked as incomplete!")
    else:
        print(f"Error: Task with ID {task_id} not found.")


def view_completed_tasks(service: TodoService):
    """Handle viewing completed tasks."""
    print("\n--- Completed Tasks ---")
    tasks = service.get_completed_tasks()
    summary = get_task_summary(tasks)
    print(f"\n{summary}")
    print("\n" + format_task_list(tasks))


def view_pending_tasks(service: TodoService):
    """Handle viewing pending tasks."""
    print("\n--- Pending Tasks ---")
    tasks = service.get_pending_tasks()
    summary = get_task_summary(tasks)
    print(f"\n{summary}")
    print("\n" + format_task_list(tasks))


def main():
    """Main function to run the Todo Console App."""
    service = TodoService()

    print("Welcome to the Todo Console App!")

    while True:
        display_menu()
        choice = get_user_input("\nEnter your choice (0-8): ")

        if choice == "0":
            print("Thank you for using the Todo Console App. Goodbye!")
            break
        elif choice == "1":
            add_task(service)
        elif choice == "2":
            view_all_tasks(service)
        elif choice == "3":
            update_task(service)
        elif choice == "4":
            delete_task(service)
        elif choice == "5":
            mark_task_complete(service)
        elif choice == "6":
            mark_task_incomplete(service)
        elif choice == "7":
            view_completed_tasks(service)
        elif choice == "8":
            view_pending_tasks(service)
        else:
            print("Invalid choice. Please enter a number between 0-8.")

        # Pause to let user see the result before showing menu again
        input("\nPress Enter to continue...")


if __name__ == "__main__":
    main()
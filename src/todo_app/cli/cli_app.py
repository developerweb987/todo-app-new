"""Command-line interface for the Todo Console App."""

import argparse
from typing import Optional
from src.todo_app.services.todo_service import TodoService


class TodoCLI:
    """Command-line interface for interacting with the Todo service."""

    def __init__(self, service: TodoService):
        """Initialize the CLI with a Todo service."""
        self.service = service
        self.parser = self._create_parser()

    def _create_parser(self) -> argparse.ArgumentParser:
        """Create the argument parser with all commands."""
        parser = argparse.ArgumentParser(
            description="Todo Console Application - Manage your tasks in memory",
            formatter_class=argparse.RawDescriptionHelpFormatter,
            epilog="""
Examples:
  Add a task:           python -m src.todo_app.main add --title "Buy groceries" --description "Milk, bread, eggs"
  List all tasks:       python -m src.todo_app.main list
  Update a task:        python -m src.todo_app.main update --id 1 --title "New title"
  Delete a task:        python -m src.todo_app.main delete --id 1
  Mark complete:        python -m src.todo_app.main complete --id 1
  Mark incomplete:      python -m src.todo_app.main incomplete --id 1
            """.strip()
        )

        subparsers = parser.add_subparsers(dest='command', help='Available commands', required=True)

        # Add command
        add_parser = subparsers.add_parser('add', help='Add a new task')
        add_parser.add_argument('--title', required=True, help='Task title (required)')
        add_parser.add_argument('--description', default='', help='Task description (optional)')

        # List command
        list_parser = subparsers.add_parser('list', help='List all tasks')
        list_parser.add_argument('--status', choices=['all', 'completed', 'pending'],
                                 default='all', help='Filter tasks by status (default: all)')

        # Update command
        update_parser = subparsers.add_parser('update', help='Update an existing task')
        update_parser.add_argument('--id', type=int, required=True, help='Task ID')
        update_parser.add_argument('--title', help='New task title')
        update_parser.add_argument('--description', help='New task description')

        # Delete command
        delete_parser = subparsers.add_parser('delete', help='Delete a task')
        delete_parser.add_argument('--id', type=int, required=True, help='Task ID')

        # Complete command
        complete_parser = subparsers.add_parser('complete', help='Mark task as complete')
        complete_parser.add_argument('--id', type=int, required=True, help='Task ID')

        # Incomplete command
        incomplete_parser = subparsers.add_parser('incomplete', help='Mark task as incomplete')
        incomplete_parser.add_argument('--id', type=int, required=True, help='Task ID')

        return parser

    def run(self, args: Optional[list] = None) -> None:
        """Parse arguments and execute the appropriate command."""
        parsed_args = self.parser.parse_args(args)

        if parsed_args.command == 'add':
            self._add_task(parsed_args)
        elif parsed_args.command == 'list':
            self._list_tasks(parsed_args)
        elif parsed_args.command == 'update':
            self._update_task(parsed_args)
        elif parsed_args.command == 'delete':
            self._delete_task(parsed_args)
        elif parsed_args.command == 'complete':
            self._complete_task(parsed_args)
        elif parsed_args.command == 'incomplete':
            self._incomplete_task(parsed_args)
        else:
            self.parser.print_help()

    def _add_task(self, args) -> None:
        """Handle the add command."""
        try:
            task = self.service.add_task(args.title, args.description)
            print(f"Task added successfully!")
            print(f"ID: {task.id}, Title: {task.title}, Description: {task.description}, Completed: {task.completed}")
        except ValueError as e:
            print(f"Error: {e}")

    def _list_tasks(self, args) -> None:
        """Handle the list command."""
        if args.status == 'completed':
            tasks = self.service.get_completed_tasks()
            print("Completed Tasks:")
        elif args.status == 'pending':
            tasks = self.service.get_pending_tasks()
            print("Pending Tasks:")
        else:  # all
            tasks = self.service.get_all_tasks()
            print("All Tasks:")

        if not tasks:
            print("No tasks found.")
        else:
            for task in tasks:
                status = "✓" if task.completed else "○"
                print(f"  {status} [{task.id}] {task.title}")
                if task.description:
                    print(f"      {task.description}")

    def _update_task(self, args) -> None:
        """Handle the update command."""
        try:
            result = self.service.update_task(args.id, args.title, args.description)
            if result:
                print(f"Task {args.id} updated successfully!")
                updated_task = self.service.get_task(args.id)
                print(f"ID: {updated_task.id}, Title: {updated_task.title}, Description: {updated_task.description}, Completed: {updated_task.completed}")
            else:
                print(f"Error: Task with ID {args.id} not found.")
        except ValueError as e:
            print(f"Error: {e}")

    def _delete_task(self, args) -> None:
        """Handle the delete command."""
        result = self.service.delete_task(args.id)
        if result:
            print(f"Task {args.id} deleted successfully!")
        else:
            print(f"Error: Task with ID {args.id} not found.")

    def _complete_task(self, args) -> None:
        """Handle the complete command."""
        result = self.service.mark_complete(args.id)
        if result:
            print(f"Task {args.id} marked as complete!")
        else:
            print(f"Error: Task with ID {args.id} not found.")

    def _incomplete_task(self, args) -> None:
        """Handle the incomplete command."""
        result = self.service.mark_incomplete(args.id)
        if result:
            print(f"Task {args.id} marked as incomplete!")
        else:
            print(f"Error: Task with ID {args.id} not found.")
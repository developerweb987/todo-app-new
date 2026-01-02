# Quickstart Guide: Todo In-Memory Python Console App

## Prerequisites
- Python 3.13 or higher
- pip package manager

## Setup
1. Clone the repository
2. Navigate to the project directory
3. Install dependencies: `pip install -r requirements.txt`
4. Run the application: `python -m src.todo_app.main`

## Basic Usage
- Add a task: `python -m src.todo_app.main add --title "Task Title" --description "Task Description"`
- View all tasks: `python -m src.todo_app.main list`
- Update a task: `python -m src.todo_app.main update --id 1 --title "New Title" --description "New Description"`
- Delete a task: `python -m src.todo_app.main delete --id 1`
- Mark complete: `python -m src.todo_app.main complete --id 1`
- Mark incomplete: `python -m src.todo_app.main incomplete --id 1`

## Project Structure
- `src/todo_app/models/task.py` - Task data model
- `src/todo_app/services/todo_service.py` - Core business logic
- `src/todo_app/cli/cli_app.py` - Command-line interface
- `tests/` - Unit and integration tests
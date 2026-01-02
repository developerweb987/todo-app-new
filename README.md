# Todo In-Memory Python Console App

A simple console-based todo application written in Python that stores tasks in memory.

## Features

- Add tasks with ID, title, description, and status
- Delete tasks by ID
- Update task title/description by ID
- View task list with status
- Mark tasks as complete/incomplete

## Requirements

- Python 3.13 or higher

## Installation

1. Clone the repository
2. Navigate to the `src` directory
3. Run the application using Python's module execution

## Usage

To run the application:

```bash
cd src
python -m todo_app.main
```

## Folder Structure

```
src/
├── todo_app/
│   ├── __init__.py
│   ├── main.py
│   ├── services/
│   │   ├── __init__.py
│   │   └── todo_service.py
│   ├── models/
│   │   ├── __init__.py
│   │   └── task.py
│   └── utils/
│       ├── __init__.py
│       └── utils.py
specs/
README.md
CLAUDE.md
```

## How to Use

1. Run the application as shown above
2. Choose an option from the menu:
   - 1: Add a new task
   - 2: View all tasks
   - 3: Update an existing task
   - 4: Delete a task
   - 5: Mark a task as complete
   - 6: Mark a task as incomplete
   - 7: View completed tasks
   - 8: View pending tasks
   - 0: Exit the application

## Architecture

- `models/task.py`: Defines the Task data model
- `services/todo_service.py`: Contains the business logic for managing tasks
- `utils/utils.py`: Provides utility functions for formatting and validation
- `main.py`: Implements the console interface and user interaction

## Design Decisions

- All imports are relative to the `todo_app` package
- Tasks are stored in memory for simplicity
- The application follows a service-oriented architecture
- Input validation is performed to ensure data integrity
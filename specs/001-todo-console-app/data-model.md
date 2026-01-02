# Data Model: Todo In-Memory Python Console App

## Task Entity

**Definition**: Represents a single todo item that can be managed by the user

**Fields**:
- `id` (int): Unique identifier for the task, auto-incremented
- `title` (str): Task title (required, max 100 characters)
- `description` (str): Task description (optional, max 500 characters)
- `completed` (bool): Completion status (default: False)
- `created_at` (datetime): Timestamp when task was created

**Validation Rules**:
- Title must not be empty or only whitespace
- Title must be between 1 and 100 characters
- Description can be empty or up to 500 characters
- ID must be unique within the application session
- ID must be a positive integer

**State Transitions**:
- `incomplete` → `complete`: When user marks task as done
- `complete` → `incomplete`: When user marks task as undone

## TodoList Collection

**Definition**: Container for managing multiple Task entities

**Operations**:
- `add_task(title, description)`: Creates new task with unique ID
- `get_task(task_id)`: Retrieves specific task by ID
- `get_all_tasks()`: Returns all tasks in the list
- `update_task(task_id, title, description)`: Modifies existing task
- `delete_task(task_id)`: Removes task from list
- `mark_complete(task_id)`: Sets task status to completed
- `mark_incomplete(task_id)`: Sets task status to incomplete
- `get_completed_tasks()`: Returns only completed tasks
- `get_pending_tasks()`: Returns only pending tasks

**Constraints**:
- Maximum 10,000 tasks in memory at one time
- Task IDs are sequential starting from 1
- No duplicate IDs allowed
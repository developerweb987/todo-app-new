# Data Model: Full-Stack Web Todo Application

## Entity Definitions

### User Entity
**Description**: Represents a registered user of the application with unique identification and authentication credentials

**Fields**:
- `id` (UUID/string): Unique identifier for the user (primary key)
- `email` (string): User's email address (unique, required)
- `username` (string): User's display name (optional)
- `created_at` (timestamp): Timestamp when the user account was created
- `updated_at` (timestamp): Timestamp when the user account was last updated
- `is_active` (boolean): Whether the account is active (default: true)

**Relationships**:
- One User to Many TodoTasks (via foreign key in TodoTask)

**Validation Rules**:
- Email must be a valid email format
- Email must be unique across all users
- Username must be unique if provided
- Email is required for account creation

### TodoTask Entity
**Description**: Represents a personal task with properties including title, description, completion status, creation timestamp, and ownership reference to a User

**Fields**:
- `id` (UUID/string): Unique identifier for the task (primary key)
- `title` (string): Title/description of the task (required, max length: 255)
- `description` (string): Optional detailed description of the task (optional, max length: 1000)
- `is_completed` (boolean): Whether the task is completed (default: false)
- `user_id` (UUID/string): Foreign key reference to the owning user (required)
- `created_at` (timestamp): Timestamp when the task was created
- `updated_at` (timestamp): Timestamp when the task was last updated

**Relationships**:
- Many TodoTasks to One User (via user_id foreign key)

**Validation Rules**:
- Title is required and cannot be empty
- Title must be less than 255 characters
- Description, if provided, must be less than 1000 characters
- user_id must reference an existing User
- Only the owning user can modify/delete the task

## State Transitions

### TodoTask State Transitions
- **Created**: New task is created with `is_completed = false`
- **Updated**: Task details (title, description) can be modified by owner
- **Completed**: `is_completed` is changed from `false` to `true` by owner
- **Reopened**: `is_completed` is changed from `true` to `false` by owner
- **Deleted**: Task is permanently removed by owner

## Indexes and Performance Considerations

### Required Indexes
- User.email (unique index for authentication performance)
- TodoTask.user_id (index for efficient user-based queries)
- TodoTask.created_at (index for chronological sorting)

### Query Patterns
- Retrieve all tasks for a specific user (filtered by user_id)
- Retrieve completed/incomplete tasks for a specific user
- Sort tasks by creation date
- Update task completion status by task ID and user context
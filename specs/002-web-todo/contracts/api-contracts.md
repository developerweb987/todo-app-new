# API Contracts: Full-Stack Web Todo Application

## Authentication Endpoints

### POST /api/auth/register
**Description**: Register a new user account

**Request**:
- Headers: `Content-Type: application/json`
- Body:
  ```json
  {
    "email": "string (required)",
    "password": "string (required, min 8 chars)"
  }
  ```

**Response**:
- 201 Created: User successfully registered
  ```json
  {
    "success": true,
    "message": "User registered successfully"
  }
  ```
- 400 Bad Request: Invalid input data
- 409 Conflict: Email already exists

### POST /api/auth/login
**Description**: Authenticate user and return session information

**Request**:
- Headers: `Content-Type: application/json`
- Body:
  ```json
  {
    "email": "string (required)",
    "password": "string (required)"
  }
  ```

**Response**:
- 200 OK: Authentication successful
  ```json
  {
    "success": true,
    "user": {
      "id": "string",
      "email": "string"
    }
  }
  ```
- 401 Unauthorized: Invalid credentials

## Todo Management Endpoints

### GET /api/todos
**Description**: Retrieve all todos for the authenticated user

**Request**:
- Headers: `Authorization: Bearer {JWT_TOKEN}`
- Query Parameters: None

**Response**:
- 200 OK: Todos retrieved successfully
  ```json
  {
    "todos": [
      {
        "id": "string",
        "title": "string",
        "description": "string (nullable)",
        "is_completed": "boolean",
        "user_id": "string",
        "created_at": "timestamp",
        "updated_at": "timestamp"
      }
    ]
  }
  ```
- 401 Unauthorized: Invalid or missing JWT token
- 403 Forbidden: User not authorized to access these resources

### POST /api/todos
**Description**: Create a new todo for the authenticated user

**Request**:
- Headers: `Authorization: Bearer {JWT_TOKEN}`, `Content-Type: application/json`
- Body:
  ```json
  {
    "title": "string (required)",
    "description": "string (optional)"
  }
  ```

**Response**:
- 201 Created: Todo created successfully
  ```json
  {
    "id": "string",
    "title": "string",
    "description": "string (nullable)",
    "is_completed": "boolean",
    "user_id": "string",
    "created_at": "timestamp",
    "updated_at": "timestamp"
  }
  ```
- 400 Bad Request: Invalid input data
- 401 Unauthorized: Invalid or missing JWT token

### PUT /api/todos/{todo_id}
**Description**: Update an existing todo for the authenticated user

**Request**:
- Path Parameter: `todo_id` (string)
- Headers: `Authorization: Bearer {JWT_TOKEN}`, `Content-Type: application/json`
- Body:
  ```json
  {
    "title": "string (optional)",
    "description": "string (optional)",
    "is_completed": "boolean (optional)"
  }
  ```

**Response**:
- 200 OK: Todo updated successfully
  ```json
  {
    "id": "string",
    "title": "string",
    "description": "string (nullable)",
    "is_completed": "boolean",
    "user_id": "string",
    "created_at": "timestamp",
    "updated_at": "timestamp"
  }
  ```
- 400 Bad Request: Invalid input data
- 401 Unauthorized: Invalid or missing JWT token
- 403 Forbidden: User not authorized to modify this todo
- 404 Not Found: Todo does not exist

### PATCH /api/todos/{todo_id}/complete
**Description**: Toggle completion status of a todo

**Request**:
- Path Parameter: `todo_id` (string)
- Headers: `Authorization: Bearer {JWT_TOKEN}`, `Content-Type: application/json`
- Body:
  ```json
  {
    "is_completed": "boolean (required)"
  }
  ```

**Response**:
- 200 OK: Todo completion status updated
  ```json
  {
    "id": "string",
    "title": "string",
    "description": "string (nullable)",
    "is_completed": "boolean",
    "user_id": "string",
    "created_at": "timestamp",
    "updated_at": "timestamp"
  }
  ```
- 400 Bad Request: Invalid input data
- 401 Unauthorized: Invalid or missing JWT token
- 403 Forbidden: User not authorized to modify this todo
- 404 Not Found: Todo does not exist

### DELETE /api/todos/{todo_id}
**Description**: Delete a todo for the authenticated user

**Request**:
- Path Parameter: `todo_id` (string)
- Headers: `Authorization: Bearer {JWT_TOKEN}`

**Response**:
- 204 No Content: Todo deleted successfully
- 401 Unauthorized: Invalid or missing JWT token
- 403 Forbidden: User not authorized to delete this todo
- 404 Not Found: Todo does not exist

## Error Response Format

All error responses follow this format:
```json
{
  "success": false,
  "error": {
    "code": "string",
    "message": "string",
    "details": "object (optional)"
  }
}
```

## Common HTTP Status Codes

- 200 OK: Request successful
- 201 Created: Resource created successfully
- 204 No Content: Request successful, no content to return
- 400 Bad Request: Invalid request parameters or body
- 401 Unauthorized: Missing or invalid authentication
- 403 Forbidden: Valid authentication but insufficient permissions
- 404 Not Found: Requested resource does not exist
- 409 Conflict: Request conflicts with current state
- 500 Internal Server Error: Unexpected server error
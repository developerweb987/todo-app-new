# Full-Stack Web Todo Application

A secure, multi-user todo application with persistent storage and JWT authentication.

## Features

- User registration and authentication
- Secure JWT-based authentication
- Create, read, update, and delete personal todo tasks
- Mark tasks as complete/incomplete
- Data isolation between users
- Responsive web interface

## Tech Stack

### Backend
- **Framework**: FastAPI (Python)
- **ORM**: SQLModel
- **Database**: PostgreSQL (Neon Serverless)
- **Authentication**: JWT tokens with middleware

### Frontend
- **Framework**: Next.js 14+ with App Router
- **Language**: TypeScript
- **Styling**: Tailwind CSS
- **API Client**: Axios with interceptors

## Setup Instructions

### Prerequisites
- Node.js 18+
- Python 3.11+
- PostgreSQL-compatible database (Neon Serverless recommended)

### Backend Setup
1. Navigate to the backend directory: `cd backend`
2. Install dependencies: `pip install -r requirements.txt`
3. Set up environment variables (see `.env.example` below)
4. Run the application: `uvicorn src.main:app --reload`

### Frontend Setup
1. Navigate to the frontend directory: `cd frontend`
2. Install dependencies: `npm install`
3. Set up environment variables (see `.env.local.example` below)
4. Run the development server: `npm run dev`

### Authentication
- `POST /api/auth/register` - Register a new user
- `POST /api/auth/login` - Log in an existing user

### Todo Operations
- `GET /api/todos` - Get all todos for the authenticated user
- `POST /api/todos` - Create a new todo
- `GET /api/todos/{id}` - Get a specific todo
- `PUT /api/todos/{id}` - Update a specific todo
- `PATCH /api/todos/{id}/complete` - Toggle completion status
- `DELETE /api/todos/{id}` - Delete a specific todo

## Architecture

The application follows a clean architecture with:

- **Models** in `backend/src/models/` - Define data structures
- **Services** in `backend/src/services/` - Business logic
- **API Routes** in `backend/src/api/` - Expose functionality via REST endpoints
- **Middleware** in `backend/src/middleware/` - Handle authentication and authorization
- **Components** in `frontend/src/components/` - Reusable UI elements
- **Pages** in `frontend/src/app/` - Define application routes and views

## Security

- JWT tokens for authentication
- User-based authorization to ensure data isolation
- Password hashing with bcrypt
- Input validation and sanitization

## Development

This project was generated using the Spec-Driven Development methodology with Claude Code. All features are traceable to specifications in the `specs/` directory.

## License

MIT

# Quickstart Guide: Full-Stack Web Todo Application

## Prerequisites

- Node.js 18+ (for frontend development)
- Python 3.11+ (for backend development)
- PostgreSQL-compatible database (Neon Serverless recommended)
- Git
- Package managers: npm/yarn/pnpm and pip

## Environment Setup

### 1. Clone the Repository
```bash
git clone <repository-url>
cd <repository-directory>
```

### 2. Backend Setup
```bash
cd backend
pip install -r requirements.txt
```

### 3. Frontend Setup
```bash
cd frontend
npm install
```

## Configuration

### 1. Backend Configuration
Create a `.env` file in the backend directory:
```env
DATABASE_URL=postgresql://username:password@localhost:5432/todo_app
SECRET_KEY=your-super-secret-jwt-key-here
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
```

### 2. Frontend Configuration
Create a `.env.local` file in the frontend directory:
```env
NEXT_PUBLIC_API_BASE_URL=http://localhost:8000
NEXT_PUBLIC_BETTER_AUTH_URL=http://localhost:3000
```

## Running the Application

### 1. Start the Backend
```bash
cd backend
python -m uvicorn src.main:app --reload --port 8000
```
The backend API will be available at `http://localhost:8000`.

### 2. Start the Frontend
```bash
cd frontend
npm run dev
```
The frontend will be available at `http://localhost:3000`.

## Development Workflow

### Backend Development
1. Define models in `src/models/`
2. Create services in `src/services/`
3. Build API routes in `src/api/`
4. Add middleware in `src/middleware/`
5. Run tests with `pytest`

### Frontend Development
1. Create components in `src/components/`
2. Build pages in `src/pages/`
3. Implement services in `src/services/`
4. Add styling with Tailwind classes
5. Run tests with Jest

## API Documentation
- Backend API documentation available at `http://localhost:8000/docs` (Swagger UI)
- Frontend API client located in `src/services/api-client.ts`

## Database Migrations
Run database migrations using Alembic:
```bash
cd backend
alembic revision --autogenerate -m "migration message"
alembic upgrade head
```

## Testing
### Backend Tests
```bash
cd backend
pytest tests/
```

### Frontend Tests
```bash
cd frontend
npm test
```
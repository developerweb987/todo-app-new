# Running the Todo Application

## Prerequisites
- Python 3.8+
- All dependencies from requirements.txt installed

## Setup Instructions

1. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Initialize the database:**
   ```bash
   python init_db.py
   ```

3. **Run the application:**
   ```bash
   # Navigate to the backend directory
   cd backend

   # Start the FastAPI server
   python -m uvicorn src.main:app --reload --host 0.0.0.0 --port 8000
   ```

## Alternative Method
If the above doesn't work, try:
```bash
cd backend
uvicorn src.main:app --reload --host 0.0.0.0 --port 8000
```

## Access the Application
Once the server is running, you can access:
- API Documentation: http://localhost:8000/docs
- Health Check: http://localhost:8000/health
- API Root: http://localhost:8000/

## Environment Variables
The application uses environment variables defined in `backend/.env` for configuration.

## Troubleshooting
- If you get a "command not found" error for uvicorn, ensure it's installed: `pip install uvicorn`
- Make sure you're in the backend directory when running the uvicorn command
- Port 8000 must be available
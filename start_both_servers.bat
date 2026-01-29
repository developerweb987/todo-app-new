@echo off
REM Script to run both frontend and backend for the Todo Application

echo Starting the Todo Application...

echo.
echo Step 1: Ensure backend is running on port 8000
echo If you get a port binding error, check if another process is using port 8000
echo You can check with: netstat -ano ^| findstr :8000

echo.
echo Step 2: Initialize database if not already done
python init_db.py

echo.
echo Step 3: Starting backend server in a new window...
start cmd /k "cd backend && echo Starting backend server... && python -m uvicorn src.main:app --host 0.0.0.0 --port 8000"

echo.
echo Step 4: Starting frontend server in a new window...
echo Make sure you're in the frontend directory and have installed dependencies with npm install
start cmd /k "cd frontend && echo Starting frontend server... && npm run dev"

echo.
echo Servers should now be running!
echo - Backend API: http://localhost:8000
echo - Frontend: http://localhost:3000 (usually)
echo - API Documentation: http://localhost:8000/docs
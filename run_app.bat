@echo off
REM Script to run the Todo Application

echo Initializing the database...
python init_db.py

echo.
echo Starting the FastAPI server...
cd backend
echo Running: python -m uvicorn src.main:app --reload --host 0.0.0.0 --port 8000
echo Visit http://localhost:8000/docs for API documentation
echo Press Ctrl+C to stop the server
echo.

python -m uvicorn src.main:app --reload --host 0.0.0.0 --port 8000
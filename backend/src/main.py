from fastapi import FastAPI, Request
from fastapi.responses import Response, JSONResponse
from fastapi.exceptions import HTTPException
from starlette.middleware.cors import CORSMiddleware  # ✅ starlette middleware for Vercel
from .api.auth_router import router as auth_router
from .api.todo_router import router as todo_router
from .database.database import engine
from .models.user import User
from .models.todo_task import TodoTask
from sqlmodel import SQLModel
import base64

# Create FastAPI app instance
app = FastAPI(
    title="Todo API",
    description="A secure, multi-user todo application API",
    version="1.0.0"
)

# Startup event: create database tables
@app.on_event("startup")
def on_startup():
    try:
        SQLModel.metadata.create_all(engine)
        print("Database tables created successfully")
    except Exception as e:
        print(f"Error creating database tables: {str(e)}")

# ✅ CORS middleware for frontend and local dev
origins = [
    "https://todo-app-new-nine.vercel.app",  # Production frontend
    "http://localhost:3000"                    # Local frontend
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],  # GET, POST, PUT, DELETE, OPTIONS
    allow_headers=["*"],
)

# Root endpoint
@app.get("/")
def read_root():
    return {"message": "Welcome to the Todo API"}

# Health check
@app.get("/health")
def health_check():
    return {"status": "healthy", "service": "todo-api"}

# Favicon
@app.get("/favicon.ico", include_in_schema=False)
def favicon():
    favicon_base64 = "iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAQAAAC1+jfqAAAALklEQVR42mNk+A+EFBgYGBhoyBkGgECCjoGBgZEBCBTQyBkAVL0DAZhVqzMAAAAASUVORK5CYII="
    favicon_bytes = base64.b64decode(favicon_base64)
    return Response(content=favicon_bytes, media_type="image/x-icon", headers={"Cache-Control": "public, max-age=86400"})

@app.head("/favicon.ico", include_in_schema=False)
def favicon_head():
    return Response(headers={"Cache-Control": "public, max-age=86400"})

# Global HTTPException handler
@app.exception_handler(HTTPException)
async def http_exception_handler(request: Request, exc: HTTPException):
    return JSONResponse(
        status_code=exc.status_code,
        content={
            "success": False,
            "error": {
                "code": exc.status_code,
                "message": exc.detail,
                "details": f"HTTP {exc.status_code}: {exc.detail}"
            }
        }
    )

# Global general Exception handler
@app.exception_handler(Exception)
async def general_exception_handler(request: Request, exc: Exception):
    return JSONResponse(
        status_code=500,
        content={
            "success": False,
            "error": {
                "code": 500,
                "message": "Internal server error",
                "details": str(exc)
            }
        }
    )

# Include routers
app.include_router(auth_router)
app.include_router(todo_router)

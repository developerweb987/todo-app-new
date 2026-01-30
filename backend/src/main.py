from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import Response
from fastapi.exceptions import HTTPException
from .api.auth_router import router as auth_router
from .api.todo_router import router as todo_router
from .database.database import engine
from .models.user import User
from .models.todo_task import TodoTask
from sqlmodel import SQLModel

# Create FastAPI app instance
app = FastAPI(
    title="Todo API",
    description="A secure, multi-user todo application API",
    version="1.0.0"
)

@app.on_event("startup")
def on_startup():
    # Create database tables
    try:
        SQLModel.metadata.create_all(engine)
        print("Database tables created successfully")
    except Exception as e:
        print(f"Error creating database tables: {str(e)}")
        # Don't raise here as it might prevent the app from starting

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://todo-app-new-mu.vercel.app"],  # In production, replace with specific origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"message": "Welcome to the Todo API"}

@app.get("/health")
def health_check():
    return {"status": "healthy", "service": "todo-api"}

@app.get("/favicon.ico", include_in_schema=False)
def favicon():
    # Return a minimal transparent 16x16 pixel PNG as favicon
    import base64
    favicon_base64 = "iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAQAAAC1+jfqAAAALklEQVR42mNk+A+EFBgYGBhoyBkGgECCjoGBgZEBCBTQyBkAVL0DAZhVqzMAAAAASUVORK5CYII="
    favicon_bytes = base64.b64decode(favicon_base64)
    return Response(content=favicon_bytes, media_type="image/x-icon", headers={"Cache-Control": "public, max-age=86400"})

@app.head("/favicon.ico", include_in_schema=False)
def favicon_head():
    # Return empty response for HEAD requests to favicon
    from fastapi.responses import Response
    return Response(headers={"Cache-Control": "public, max-age=86400"})

# Global exception handler to ensure consistent error format
@app.exception_handler(HTTPException)
async def http_exception_handler(request: Request, exc: HTTPException):
    from fastapi.responses import JSONResponse
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

@app.exception_handler(Exception)
async def general_exception_handler(request: Request, exc: Exception):
    from fastapi.responses import JSONResponse
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

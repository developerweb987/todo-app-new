from fastapi import APIRouter, Depends, HTTPException, status
from sqlmodel import Session, select
from typing import Dict
from ..database.database import get_session
from ..models.user import User
from ..services.auth_service import AuthService

router = APIRouter(prefix="/api/auth", tags=["auth"])

@router.post("/register")
def register_user(user_data: Dict[str, str], session: Session = Depends(get_session)):
    try:
        # Use the AuthService to register the user
        user = AuthService.register_user(session, user_data["email"], user_data["password"])
        return {"success": True, "data": {"id": user.id, "email": user.email}}
    except HTTPException:
        # Re-raise HTTP exceptions as they contain proper error codes
        raise
    except Exception as e:
        # For other exceptions, return error response
        error_msg = str(e.detail) if hasattr(e, 'detail') else str(e)
        return {"success": False, "error": {"code": "REGISTRATION_ERROR", "message": error_msg}}

@router.post("/login")
def login_user(user_data: Dict[str, str], session: Session = Depends(get_session)):
    try:
        # Use the AuthService to authenticate the user
        user = AuthService.authenticate_user(session, user_data["email"], user_data["password"])
        if not user:
            return {"success": False, "error": {"code": "AUTHENTICATION_FAILED", "message": "Incorrect email or password"}}

        # Generate token using AuthService
        access_token = AuthService.generate_auth_token(user)

        return {
            "success": True,
            "data": {
                "access_token": access_token,
                "token_type": "bearer",
                "user": {"id": user.id, "email": user.email}
            }
        }
    except HTTPException:
        # Re-raise HTTP exceptions as they contain proper error codes
        raise
    except Exception as e:
        # For other exceptions, return error response
        error_msg = str(e.detail) if hasattr(e, 'detail') else str(e)
        return {"success": False, "error": {"code": "LOGIN_ERROR", "message": error_msg}}
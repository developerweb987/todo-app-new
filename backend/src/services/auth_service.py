from sqlmodel import Session, select
from datetime import datetime, timedelta
from jose import jwt
from passlib.context import CryptContext
from fastapi import HTTPException, status
import os
from dotenv import load_dotenv
from ..models.user import User
from typing import Optional

load_dotenv()

# Password hashing
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
MAX_PASSWORD_LENGTH = 72  # bcrypt max limit

# JWT configuration
SECRET_KEY = os.getenv("SECRET_KEY", "your-super-secret-key-change-in-production")
ALGORITHM = os.getenv("ALGORITHM", "HS256")
ACCESS_TOKEN_EXPIRE_MINUTES = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES", "30"))

class AuthService:
    @staticmethod
    def get_password_hash(password: str) -> str:
        # Truncate before hashing to avoid bcrypt >72 bytes error
        truncated = password[:MAX_PASSWORD_LENGTH]
        return pwd_context.hash(truncated)

    @staticmethod
    def verify_password(plain_password: str, hashed_password: str) -> bool:
        # Truncate before verifying
        truncated = plain_password[:MAX_PASSWORD_LENGTH]
        return pwd_context.verify(truncated, hashed_password)

    @staticmethod
    def create_access_token(data: dict, expires_delta: timedelta = None) -> str:
        to_encode = data.copy()
        if expires_delta:
            expire = datetime.utcnow() + expires_delta
        else:
            expire = datetime.utcnow() + timedelta(minutes=15)

        to_encode.update({"exp": expire})
        encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
        return encoded_jwt

    @staticmethod
    def register_user(session: Session, email: str, password: str) -> User:
        # Check if user already exists
        existing_user = session.exec(select(User).where(User.email == email)).first()
        if existing_user:
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail="Email already registered"
            )

        # Create new user with truncated password
        hashed_password = AuthService.get_password_hash(password)
        db_user = User(
            email=email,
            hashed_password=hashed_password
        )
        session.add(db_user)
        session.commit()
        session.refresh(db_user)
        return db_user

    @staticmethod
    def authenticate_user(session: Session, email: str, password: str) -> Optional[User]:
        # Find user by email
        db_user = session.exec(select(User).where(User.email == email)).first()
        if not db_user or not AuthService.verify_password(password, db_user.hashed_password):
            return None
        return db_user

    @staticmethod
    def generate_auth_token(user: User) -> str:
        # Create access token
        access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
        access_token = AuthService.create_access_token(
            data={"sub": user.id}, expires_delta=access_token_expires
        )
        return access_token

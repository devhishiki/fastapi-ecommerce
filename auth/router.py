from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

import db
from user import hashing
from user.models import User
from auth.jwt import create_access_token

router = APIRouter(tags=["auth"])


@router.post("/login")
def login(
    request: OAuth2PasswordRequestForm = Depends(),
    database: Session = Depends(db.get_db),
):
    user: User = database.query(User).filter(User.email == request.username).first()
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Invalid Credentials"
        )

    # access_token = create_access_token(data={"sub": user.email})
    access_token = create_access_token(user)
    return {"access_token": access_token, "token_type": "bearer"}

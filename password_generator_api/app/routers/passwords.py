from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.dependencies import get_current_user, get_db
from app.models import GeneratedPassword, User
from app.password_service import generate_password
from app.schemas import MessageResponse, PasswordResponse


router = APIRouter(
    prefix="/password",
    tags=["Passwords"],
)


@router.post("/new", response_model=PasswordResponse, status_code=status.HTTP_201_CREATED)
def create_password(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    while True:
        password = generate_password()

        existing_password = (
            db.query(GeneratedPassword)
            .filter(GeneratedPassword.password == password)
            .first()
        )

        if existing_password is None:
            break

    new_password = GeneratedPassword(
        user_id=current_user.id,
        password=password,
    )

    db.add(new_password)
    db.commit()
    db.refresh(new_password)

    return PasswordResponse(
        username=current_user.username,
        password=new_password.password,
        created_at=new_password.created_at,
    )
@router.get("/{username}", response_model=list[PasswordResponse])
def get_user_passwords(
    username: str,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    if current_user.username != username:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="You can only access your own passwords",
        )

    passwords = (
        db.query(GeneratedPassword)
        .filter(GeneratedPassword.user_id == current_user.id)
        .all()
    )

    return [
        PasswordResponse(
            username=current_user.username,
            password=password.password,
            created_at=password.created_at,
        )
        for password in passwords
    ]
@router.delete("/{username}/{password}", response_model=MessageResponse)
def delete_user_password(
    username: str,
    password: str,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    if current_user.username != username:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="You can only delete your own passwords",
        )

    deleted_count = (
        db.query(GeneratedPassword)
        .filter(
            GeneratedPassword.user_id == current_user.id,
            GeneratedPassword.password == password,
        )
        .delete()
    )

    db.commit()

    if deleted_count == 0:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Password not found",
        )

    return MessageResponse(message="Password deleted successfully")
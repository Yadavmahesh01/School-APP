from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from database import SessionLocal
from models import Student
from auth.utils import hash_password, verify_password
from auth.auth import create_access_token
from pydantic import BaseModel, EmailStr
from fastapi.security import OAuth2PasswordRequestForm

router = APIRouter(prefix="/auth", tags=["Auth"])

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

        
@router.get("/debug")
def debug(db: Session = Depends(get_db)):
    users = db.query(Student).all()

    return [
        {
            "email": u.email,
            "hash": u.hashed_password
        }
        for u in users
    ]

# ✅ ADD THIS BACK
class StudentSignup(BaseModel):
    name: str
    email: EmailStr
    password: str


# 🔹 SIGN UP
@router.post("/signup")
def signup(student: StudentSignup, db: Session = Depends(get_db)):

    existing_user = db.query(Student).filter(Student.email == student.email).first()
    if existing_user:
        raise HTTPException(status_code=400, detail="Email already registered")

    hashed_pw = hash_password(student.password)

    new_student = Student(
        name=student.name,
        email=student.email,
        hashed_password=hashed_pw
    )

    db.add(new_student)
    db.commit()
    db.refresh(new_student)

    return {"message": "Student registered successfully"}


# 🔹 LOGIN (OAuth2 Correct Version)
@router.post("/login")
def login(
    form_data: OAuth2PasswordRequestForm = Depends(),
    db: Session = Depends(get_db)
):

    user = db.query(Student).filter(
        Student.email == form_data.username
    ).first()

    if not user:
        raise HTTPException(status_code=401, detail="Invalid email")

    print("Entered Password:", form_data.password)
    print("Stored Hash:", user.hashed_password)

    result = verify_password(
        form_data.password,
        user.hashed_password
    )

    print("Verify Result:", result)

    if not result:
        raise HTTPException(status_code=401, detail="Invalid password")

    token = create_access_token({
        "sub": user.email,
        "role": user.role
    })

    return {
        "access_token": token,
        "token_type": "bearer"
    }
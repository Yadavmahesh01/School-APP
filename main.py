from fastapi import FastAPI
from database import engine
from models import Base
from auth.routes import router as auth_router
from student.routes import router as student_router
from teacher.routes import router as teacher_router


from auth.routes import router as auth_router

Base.metadata.create_all(bind=engine)

app = FastAPI()
app.include_router(auth_router)
app.include_router(student_router)
app.include_router(teacher_router)
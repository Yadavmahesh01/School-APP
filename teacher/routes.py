from fastapi import APIRouter, Depends,HTTPException
from pydantic import BaseModel
from auth.auth import teacher_only
import json

router = APIRouter(prefix="/teacher", tags=["Teacher"])

DATA_FILE = "data/student_data.json"


class Student(BaseModel):
    name: str
    email: str
    course_branch: str


@router.post("/student/{student_id}",status_code=200)
def add_student(student_id: str, student: Student, user=Depends(teacher_only)):

    with open(DATA_FILE, "r") as f:
        data = json.load(f)

    data[student_id] = student.dict()

    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=4)

    return {"message": "Student added successfully"}

@router.delete("/student/{student_id}",status_code=200)
def remove_student(student_id:str,student: Student,user=Depends(teacher_only)):
    try:
        with open(DATA_FILE,"r") as f:
            data=json.load(f)
    except FileNotFoundError :
        raise HTTPException(status_code=500,description="File Not Found Error the data is missing")  
          
    del data[student_id]      

    if student_id not in data:
        raise HTTPException(status_code=404,description="Student_id not found in the database")
    with open(DATA_FILE,'w') as f:
        data=json.load(data,f,indent=4)  
    return {"message: Student Removed Successfully"}

@router.put("/student/{student_id}")
def update_student_info(student_id:str,student=Student,user=Depends(teacher_only)):
    try:
        with open(DATA_FILE,"r") as f:
            data=json.load(f)
    except FileNotFoundError:
        raise HTTPException(status_code=500,descryption="File not found")
    
    if student_id not in data:
        raise HTTPException(status_code=404,descryption="Student_id not found error")
    
    data[student_id]=student.dict()

    with open(DATA_FILE,"w") as f:
        json.dump(data,f,indent=4)
    return {"message":"Student info updated successfully"}    

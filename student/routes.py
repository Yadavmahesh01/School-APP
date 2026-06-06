from fastapi import APIRouter, HTTPException, Depends
import json
from auth.auth import student_only

router = APIRouter(prefix="/student", tags=["Student"])

DATA_FILE = "data/student_data.json"


def load_data():
    with open(DATA_FILE, "r") as f:
        return json.load(f)


@router.get("/view")
def view_students(user=Depends(student_only)):
    return load_data()


@router.get("/{student_id}")
def student_view(student_id: str, user=Depends(student_only)):
    data = load_data()

    if student_id in data:
        return data[student_id]

    raise HTTPException(status_code=404, detail="Student not found")
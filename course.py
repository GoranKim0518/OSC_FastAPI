from fastapi import APIRouter, HTTPException, status
from model import Course
import json

course_router = APIRouter()

JSON_FILE = "courses.json"

def load_courses():
    try:
        with open(JSON_FILE, "r", encoding="utf-8") as f:
            return json.load(f)

    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=str(e)
        )

def save_courses(data):
    try:
        with open(JSON_FILE, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)

    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=str(e)
        )

@course_router.post("/courses")
async def add_course(course: Course):
    courses_list = load_courses()
    courses_list.append(course.model_dump())
    save_courses(courses_list)
    return {
        "msg": "course post success",
        "course": course
    }

@course_router.get("/courses")
async def retrieve_courses():
    courses_list = load_courses()
    return {
        "courses": courses_list
    }

#@course_router.get("/todo/{todo_id}")
#async def get_single_todo(todo_id: int = Path(..., title = "the ID of the todo to retrieve")) -> dict:
#    for todo in courses_list:
#        if todo.id == todo_id:
#            return { "todo" : todo}
#    return {"msg" : "todo with supplied ID doesn't exist"}
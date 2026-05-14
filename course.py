from fastapi import APIRouter
from model import Course

course_router = APIRouter()

courses_list = []

@course_router.post("/courses")
async def add_course(course: Course) -> dict:
    courses_list.append(course)
    return {
        "msg": "course post success"
    }   #try-catch 추가

@course_router.get("/courses")
async def retrieve_courses() -> dict:
    return {
        "courses": courses_list
    }
        #json import로 변경


        
#@course_router.get("/todo/{todo_id}")
#async def get_single_todo(todo_id: int = Path(..., title = "the ID of the todo to retrieve")) -> dict:
#    for todo in courses_list:
#        if todo.id == todo_id:
#            return { "todo" : todo}
#    return {"msg" : "todo with supplied ID doesn't exist"}
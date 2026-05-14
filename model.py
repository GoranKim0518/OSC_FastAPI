from pydantic import BaseModel

class Course(BaseModel):
    id: int
    course_name: str
    year: int
    semester: int
    grade: str
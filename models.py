from pydantic import BaseModel


class Lesson(BaseModel):
    week_day: str
    start_time: str
    end_time: str
    lesson_number: str
    week_types: list[str] = []
    lesson_type: str
    lesson_name: str
    class_rooms: list[str] = []
    groups: list[str] = []
    teachers: list[str] = []
    building: str


class Timetable:
    lessons: list[Lesson]


class Response():
    pass

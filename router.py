from fastapi import APIRouter
from repository import LessonRepo
from models import Lesson, Timetable

router = APIRouter()


@router.post('/timetable/{group}')
async def get_group_timetable(group: str):
    obj = await LessonRepo.retrieve_group(group)
    return {'timetable': obj}


@router.post('/timetable/')
async def get_all_timetable():
    return await LessonRepo.retrieve()

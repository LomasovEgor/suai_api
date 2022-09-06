from models import Lesson
from config import database


class LessonRepo:

    @staticmethod
    async def retrieve() -> list:
        lessons = []
        collection = database.get_collection('lessons').find()
        async for lesson in collection:
            lessons.append(lesson)
        return lessons

    @staticmethod
    async def retrieve_group(group: str) -> list:
        lessons = []
        collection = database.get_collection('lessons').find({'groups': group}, {'_id': 0})
        async for lesson in collection:
            lessons.append(lesson)
        return lessons

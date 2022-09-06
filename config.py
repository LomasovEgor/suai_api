import motor.motor_asyncio
import os

MONGODB_URL = os.environ['MONGODB_URL']

client = motor.motor_asyncio.AsyncIOMotorClient(MONGODB_URL)

database = client.SUAI_timetable

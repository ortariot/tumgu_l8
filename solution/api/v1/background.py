from http import HTTPStatus

from fastapi import APIRouter, BackgroundTasks

from services.pictures import get_pictures, url
from services.clientcelery import client


back_router = APIRouter()


@back_router.post("/get_pics/")
async def get_pics(folder: str, backgroundtasks: BackgroundTasks):
    backgroundtasks.add_task(get_pictures, url, name=folder)
    return {"result": "ok"}

@back_router.post("/get_pics_celery/")
async def get_pics_celery(folder: str):
    client.send_task("tasker.task.get_pictures", args=[url, folder])

    return {"result": "ok"}
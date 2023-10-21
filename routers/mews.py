from celery import group
from fastapi import APIRouter
from starlette.responses import JSONResponse
import json
from api import handle_xml
from celery_tasks.tasks import generate_xml
from config.celery_utils import get_task_info
from schemas.mews import MewsData, OptionalSchema

router = APIRouter(prefix='/mews', tags=['Mews'], responses={404: {"description": "Not found"}})


@router.post("/xml")
async def parse_data(data: MewsData):
    """
    Send data to Parser microservice
    """
    print('Request received to send data to sender')
    print(data)
    task = generate_xml.apply_async(args=[data.model_dump()])
    return JSONResponse({"task_id": task.id})


@router.get("/task/{task_id}")
async def get_task_status(task_id: str) -> dict:
    """
    Return the status of the submitted Task
    """
    return get_task_info(task_id)

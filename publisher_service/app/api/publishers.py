from fastapi import HTTPException, APIRouter

from app.api.models import PublisherIn, PublisherOut
from app.api import db_manager

publishers = APIRouter()


@publishers.post('/', status_code=201)
async def add_publisher(payload: PublisherIn):
    publisher_id = await db_manager.add_publisher(payload)
    response = {
        'id': publisher_id,
        **payload.dict()
    }
    return response;


@publishers.get('/{id}', response_model=PublisherOut)
async def get_publisher(id: int):
    publisher = await db_manager.get_publisher(id)

    if not publisher:
        raise HTTPException(status_code=404, detail='Publisher not found')

    return publisher


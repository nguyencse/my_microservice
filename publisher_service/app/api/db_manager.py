from app.api.models import PublisherIn
from app.api.db import publishers, database

async def add_publisher(payload: PublisherIn):
    query = publishers.insert().values(**payload.dict())
    return await database.execute(query=query)


async def get_publisher(id):
    query = publishers.select(publishers.c.id == id)
    return await database.fetch_one(query=query)
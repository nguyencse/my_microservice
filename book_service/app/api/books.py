from typing import List
from fastapi import HTTPException, APIRouter

from app.api.models import BookIn, BookOut
from app.api.service import is_publisher_present
from app.api import db_manager

books = APIRouter()

@books.get('/', response_model=List[BookOut])
async def get_books():
    return await db_manager.get_all_books()

@books.get('/{id}', response_model=BookOut)
async def get_book(id: int):
    book = await db_manager.get_book(id)
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")
    return book

@books.post('/', status_code=201)
async def add_book(payload: BookIn):
    if not is_publisher_present(payload.publisher_id):
        raise HTTPException(status_code=404, detail=f"Publisher with id:{payload.publisher_id} not found")

    book_id = await db_manager.add_book(payload)
    response = {
        'id': book_id,
        **payload.dict()
    }
    return response

@books.put('/{id}', response_model=BookOut)
async def update_book(id: int, payload: BookIn):
    book = await db_manager.get_book(id)
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")

    update_data = payload.dict(exclude_unset=True)
    book_in_db = BookIn(**book)
    
    updated_book = book_in_db.copy(update=update_data)
    return await db_manager.update_book(id, updated_book)

@books.delete('/{id}')
async def delete_book(id: int):
    book = await db_manager.get_book(id)
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")
    return await db_manager.delete_book(id)


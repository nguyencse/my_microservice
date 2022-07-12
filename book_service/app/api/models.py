from pydantic import BaseModel
from typing import List, Optional


class BookIn(BaseModel):
    name: str
    author: str
    publisher_id: int
    language: str


class BookOut(BookIn):
    id: int


class BookUpdate(BookIn):
    name: Optional[str] = None
    author: Optional[str] = None
    publisher_id: Optional[int] = None
    language: Optional[str] = None
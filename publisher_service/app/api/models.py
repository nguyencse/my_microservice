from pydantic import BaseModel
from typing import List, Optional

class PublisherIn(BaseModel):
    name: str
    nationality: Optional[str] = None


class PublisherOut(PublisherIn):
    id: int


class PublisherUpdate(PublisherIn):
    name: Optional[str] = None
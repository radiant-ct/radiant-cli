from pydantic import BaseModel
from uuid import UUID
from typing import Optional

class DatasetCreate(BaseModel):
    name: str
    description: Optional[str] = None
    credits: Optional[str] = None


class DatasetRead(DatasetCreate):
    id: UUID

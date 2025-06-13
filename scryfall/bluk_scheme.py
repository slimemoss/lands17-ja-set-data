from pydantic import BaseModel
from uuid import UUID
from datetime import datetime


class Bluk(BaseModel):
    object: str
    id: UUID
    type: str
    updated_at: datetime
    uri: str
    name: str
    description: str
    size: int
    download_uri: str
    content_type: str
    content_encoding: str

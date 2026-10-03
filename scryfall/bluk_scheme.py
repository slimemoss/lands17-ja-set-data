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
    compressed_size: int
    jsonl_download_uri: str

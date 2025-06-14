from typing import List, Optional

from pydantic import BaseModel, RootModel


class ImageUris(BaseModel):
    small: str
    normal: str
    large: str
    png: str
    art_crop: str
    border_crop: str


class CardFace(BaseModel):
    name: str
    image_uris: Optional[ImageUris] = None


class OracleCard(BaseModel):
    name: str
    set: str
    collector_number: str
    image_uris: Optional[ImageUris] = None
    card_faces: Optional[List[CardFace]] = None


class OracleCards(RootModel):
    root: List[OracleCard]

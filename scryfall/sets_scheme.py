from enum import Enum
from pydantic import BaseModel
from uuid import UUID
from datetime import datetime
from typing import Optional, List


class Object(Enum):
    SET = "set"


class SetType(Enum):
    ALCHEMY = "alchemy"
    ARCHENEMY = "archenemy"
    ARSENAL = "arsenal"
    BOX = "box"
    COMMANDER = "commander"
    CORE = "core"
    DRAFT_INNOVATION = "draft_innovation"
    DUEL_DECK = "duel_deck"
    EXPANSION = "expansion"
    FROM_THE_VAULT = "from_the_vault"
    FUNNY = "funny"
    MASTERPIECE = "masterpiece"
    MASTERS = "masters"
    MEMORABILIA = "memorabilia"
    MINIGAME = "minigame"
    PLANECHASE = "planechase"
    PREMIUM_DECK = "premium_deck"
    PROMO = "promo"
    SPELLBOOK = "spellbook"
    STARTER = "starter"
    TOKEN = "token"
    TREASURE_CHEST = "treasure_chest"
    VANGUARD = "vanguard"


class Datum(BaseModel):
    object: Object
    id: UUID
    code: str
    name: str
    uri: str
    scryfall_uri: str
    search_uri: str
    released_at: datetime
    set_type: SetType
    card_count: int
    digital: bool
    nonfoil_only: bool
    foil_only: bool
    icon_svg_uri: str
    parent_set_code: Optional[str] = None
    tcgplayer_id: Optional[int] = None
    mtgo_code: Optional[str] = None
    arena_code: Optional[str] = None
    block_code: Optional[str] = None
    block: Optional[str] = None
    printed_size: Optional[int] = None


class Sets(BaseModel):
    object: str
    has_more: bool
    data: List[Datum]

import json
import pathlib

from pydantic import BaseModel

from scryfall.cards import Card

BACK_IMAGE_URL = 'https://backs.scryfall.io/small/2/2/222b7a3b-2321-4d4c-af19-19338b134971.jpg?1677416389'


class ImageUrlI(BaseModel):
    name: str
    url: str | None

    @classmethod
    def from_card(cls, card: Card):
        if card.image_uris is None:
            url = None
        else:
            url = card.image_uris.small
        return cls(name=card.name, url=url)


class ImageUrlsI(BaseModel):
    data: list[ImageUrlI]

    # scryfallの更新があるかを確認するのに使う
    scryfall_card_count: int


class ImageUrl:
    code: str

    def __init__(self, code: str) -> None:
        self.code = code

    def _path(self):
        return pathlib.Path('public_data', '{}.json'.format(self.code))

    def read(self) -> ImageUrlsI:
        path = self._path()
        if not path.exists():
            return ImageUrlsI(data=[], scryfall_card_count=0)

        with open(path) as f:
            try:
                res = json.load(f)
            except json.JSONDecodeError:
                return ImageUrlsI(data=[], scryfall_card_count=0)

        return ImageUrlsI(**res)

    def write(self, data: ImageUrlsI):
        self._path().parent.mkdir(parents=True, exist_ok=True)
        with open(self._path(), 'w') as f:
            json.dump(data.model_dump(), f)

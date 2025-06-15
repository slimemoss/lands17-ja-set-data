from typing import Callable, Hashable, Optional

from cache import requests
from pydantic import BaseModel

from scryfall import bluk
from scryfall.cards_scheme import ImageUris, OracleCard, OracleCards


class Card(BaseModel):
    name: str
    set: str
    collector_number: str
    image_uris: Optional[ImageUris] = None

    @classmethod
    def from_scryfall(cls, c: OracleCard) -> "Card":
        if c.card_faces is not None:
            name = c.card_faces[0].name
            image_uris = c.card_faces[0].image_uris or c.image_uris
        else:
            name = c.name
            image_uris = c.image_uris

        return Card(name=name,
                    set=c.set,
                    collector_number=c.collector_number.rjust(10, '0'),
                    image_uris=image_uris)


def primary_name(card: OracleCard):
    if card.card_faces is not None:
        return card.card_faces[0].name
    return card.name


def remove_duplicates(cards: list[Card],
                      key: Callable[[Card], Hashable]
                      ) -> list[Card]:
    seen = set()
    result = []
    for card in cards:
        k = key(card)
        if k not in seen:
            print('first: {}'.format(k))
            seen.add(k)
            result.append(card)
        else:
            print('seen : {}'.format(k))
    return result


def get():
    url = bluk.get().download_uri
    resp = requests.get(url)
    data = resp.json()
    cards = OracleCards(data).root

    cards = [Card.from_scryfall(c) for c in cards]
    cards = sorted(cards, key=lambda c: (c.set, c.collector_number))
    return remove_duplicates(cards, lambda c: (c.name, c.set))


def classify_by_set(cards: list[Card]):
    res: dict[str, list[Card]] = {}

    for card in cards:
        code = card.set
        cards_by_set = res.get(code, []) + [card]
        res[code] = cards_by_set

    for k in res.keys():
        res[k] = sorted(res[k], key=lambda c: c.collector_number)

    return res

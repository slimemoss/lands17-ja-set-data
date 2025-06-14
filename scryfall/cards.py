from cache import requests

from scryfall import bluk, cards_scheme


def primary_name(card: cards_scheme.OracleCard):
    if card.card_faces is not None:
        return card.card_faces[0].name
    return card.name


def remove_duplicates(cards: list[cards_scheme.OracleCard]) -> list[cards_scheme.OracleCard]:
    cards = sorted(cards, key=lambda c: c.collector_number.rjust(10, '0'))

    seen = set()
    result = []
    for card in cards:
        key = (card.set, primary_name(card))
        if key not in seen:
            seen.add(key)
            result.append(card)
    return result


def get():
    url = bluk.get().download_uri
    resp = requests.get(url)
    data = resp.json()

    cards = cards_scheme.OracleCards(data).root
    return remove_duplicates(cards)


def classify_by_set(cards: list[cards_scheme.OracleCard]):
    res: dict[str, list[cards_scheme.OracleCard]] = {}

    for card in cards:
        code = card.set
        cards_by_set = res.get(code, []) + [card]
        res[code] = cards_by_set

    return res

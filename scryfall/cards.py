from cache import requests

from scryfall import bluk, cards_scheme


def get():
    url = bluk.get().download_uri
    resp = requests.get(url)
    data = resp.json()

    return cards_scheme.OracleCards(data).root


def classify_by_set(cards: list[cards_scheme.OracleCard]):
    res: dict[str, list[cards_scheme.OracleCard]] = {}

    for card in cards:
        code = card.set
        cards_by_set = res.get(code, []) + [card]
        res[code] = cards_by_set

    return res

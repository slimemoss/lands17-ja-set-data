from cache import requests

from scryfall.bluk_scheme import Bluk


def get():
    url = 'https://api.scryfall.com/bulk-data/oracle_cards'
    data = requests.get(url).json()
    return Bluk(**data)

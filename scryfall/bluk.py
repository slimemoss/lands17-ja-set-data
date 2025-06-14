from cache import requests

from scryfall.bluk_scheme import Bluk


def get():
    url = 'https://api.scryfall.com/bulk-data/unique_artwork'
    data = requests.get(url).json()
    return Bluk(**data)

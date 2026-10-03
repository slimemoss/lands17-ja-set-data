import http_client
from scryfall.bluk_scheme import Bluk


def get():
    url = 'https://api.scryfall.com/bulk-data/unique_artwork'
    data = http_client.get(url).json()
    return Bluk(**data)

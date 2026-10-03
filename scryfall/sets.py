import http_client
from scryfall import sets_scheme


def get():
    url = 'https://api.scryfall.com/sets'
    data = http_client.get(url).json()
    return sets_scheme.Sets(**data).data

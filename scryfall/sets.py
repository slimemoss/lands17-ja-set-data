from cache import requests

from scryfall import sets_scheme


def get():
    url = 'https://api.scryfall.com/sets'
    data = requests.get(url).json()
    return sets_scheme.Sets(**data).data

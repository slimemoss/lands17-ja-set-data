from cache import requests

from lands17.filters_scheme import Filters


def get_codes():
    url = 'https://www.17lands.com/data/filters'
    data = Filters(**requests.get(url).json())

    return [d.lower() for d in data.expansions]

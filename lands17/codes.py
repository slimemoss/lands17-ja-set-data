import http_client
from lands17.filters_scheme import Filters


def get_codes():
    url = 'https://www.17lands.com/data/filters'
    data = Filters(**http_client.get(url).json())

    return [d.lower() for d in data.expansions]

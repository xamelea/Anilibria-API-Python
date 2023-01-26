import requests
import json
from anilibriaAPI3.config import url
import anilibriaAPI3.auth as auth

auth.auth()


def search_title_id(name, responses=5):
    if type(name) == type(''):
        temp1 = requests.get(url=f'{url}/v3/title/search', params={'search': name, 'filter': 'id,names', 'limit': responses})
        temp2 = json.loads(temp1.text)
        try:
            return temp2['list']
        except KeyError:
            return temp2['error']
    else:
        raise Exception('search_title_id() name argument is not string')

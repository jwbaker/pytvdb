from datetime import timedelta

import requests
from ttldict import TTLOrderedDict

from .models import Series

__all__ = ['Search']


class TVDB:

    API_KEY_DEFAULT = 'FF7EF57268A992D6'
    TOKEN_CACHE = TTLOrderedDict(default_ttl=timedelta(hours=24).total_seconds())
    BASE_URL = 'https://api.thetvdb.com'

    def __init__(self, api_key=None, language='en', version=None):
        self._api_key = api_key or TVDB.API_KEY_DEFAULT
        self._language = language
        if version:
            self._version = version

    def make_request(self, route, params):
        token = self._get_token()
        headers = self._build_headers(token)
        r = requests.get(self.__class__.BASE_URL + route, params=params, headers=headers)
        r.raise_for_status()
        return r.json()

    def _build_headers(self, api_token):
        headers = {
            'Authorization': 'Bearer ' + api_token,
            'Accept-Language': self._language,
            'Accept': 'application/json'
        }

        if self._version:
            headers['Accept'] = 'application/vnd.thetvdb.v' + self._version

        return headers

    def _get_token(self):
        try:
            return self.__class__.TOKEN_CACHE['token']
        except KeyError:
            r = requests.post(self.__class__.BASE_URL + '/login', data={'apikey': self._api_key})
            r.raise_for_status()
            token = r.json()['token']
            self.__class__.TOKEN_CACHE['token'] = token
            return token


class Search(TVDB):

    def __init__(self, **kwargs):
        super(Search, self).__init__(**kwargs)

    def series(self, name='', imdb_id='', zap_2_it_id=''):
        params = {}

        if name:
            params['name'] = name
        if imdb_id:
            params['imdbId'] = imdb_id
        if zap_2_it_id:
            params['zap2itId'] = zap_2_it_id

        res = self.make_request('/search/series', params)
        return [Series(**d) for d in res]
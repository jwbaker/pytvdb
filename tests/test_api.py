import pytest
from requests import HTTPError

from pytvdb import Search


class TestSystemSearch:
    def test_search_by_name(self):
        res = Search().series(name='Doctor Who')
        assert len(res) == 12

    def test_search_by_imdb_id(self):
        res = Search().series(imdb_id='tt0436992')
        assert len(res) == 1

    def test_search_by_zap2it_id(self):
        res = Search().series(zap_2_it_id='EP00750178')
        assert len(res) == 1

    def test_search_by_name_and_imdb(self):
        with pytest.raises(HTTPError):
            assert not Search().series(name='Doctor Who', imdb_id='tt0436992')

    def test_search_by_name_and_zap2it(self):
        with pytest.raises(HTTPError):
            assert not Search().series(name='Doctor Who', zap_2_it_id='EP00750178')

    def test_search_by_zap2it_and_imdb(self):
        with pytest.raises(HTTPError):
            assert not Search().series(zap_2_it_id='EP00750178', imdb_id='tt0436992')

    def test_search_by_name_and_zap2it_and_imdb(self):
        with pytest.raises(HTTPError):
            assert not Search().series(name='Doctor Who', zap_2_it_id='EP00750178', imdb_id='tt0436992')
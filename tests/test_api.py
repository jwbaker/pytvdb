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

    def test_search_with_version(self):
        res = Search(version='2.1.1').series(name='Doctor Who')
        assert len(res) == 12

    def test_search_different_language(self):
        res = Search(language='de').series(imdb_id='tt0436992')
        assert len(res[0].aliases) == 0
        assert res[0].overview == "Die Serie handelt von einem mysteriösen Außerirdischen namens „Der Doktor“, der " \
                                  "mit seinem Raumschiff, der TARDIS (Time and Relative Dimension in Space), welches" \
                                  " von außen aussieht wie eine englische Notruf-Telefonzelle der 60er Jahre, durch" \
                                  " Raum und Zeit fliegt. Der Doktor ist ein Time Lord vom Planeten Gallifrey - und" \
                                  " bereits über 900 Jahre alt. Dass man ihm das nicht ansieht, liegt vor allem" \
                                  " daran, dass ein Time Lord, wenn er stirbt, in der Lage ist, sich zu regenerieren," \
                                  " wobei er auch eine andere Gestalt annimmt."
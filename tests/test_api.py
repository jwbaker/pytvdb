# coding=utf-8
import pytest
from requests import HTTPError

from pytvdb import TVDB


class TestTVDB:
    @pytest.mark.unit
    def test_build_list_of_models(self):

        class TestObject:
            def __init__(self, **kwargs):
                self.value = kwargs.get('value')

        data = [1, 2, 3, 4, 5]
        f = TestObject
        res = TVDB()._build_list_of_models(f, [{'value': x} for x in data])

        for val, obj in zip(data, res):
            assert val == obj.value


class TestSearch:
    @pytest.mark.system
    def test_search_by_name(self):
        res = TVDB().search().series(name='Doctor Who')
        assert len(res) == 12

    @pytest.mark.system
    def test_search_by_imdb_id(self):
        res = TVDB().search().series(imdb_id='tt0436992')
        assert len(res) == 1

    @pytest.mark.system
    def test_search_by_zap2it_id(self):
        res = TVDB().search().series(zap2it_id='EP00750178')
        assert len(res) == 1

    @pytest.mark.system
    def test_search_by_name_and_imdb(self):
        with pytest.raises(HTTPError):
            assert not TVDB().search().series(name='Doctor Who', imdb_id='tt0436992')

    @pytest.mark.system
    def test_search_by_name_and_zap2it(self):
        with pytest.raises(HTTPError):
            assert not TVDB().search().series(name='Doctor Who', zap2it_id='EP00750178')

    @pytest.mark.system
    def test_search_by_zap2it_and_imdb(self):
        with pytest.raises(HTTPError):
            assert not TVDB().search().series(zap2it_id='EP00750178', imdb_id='tt0436992')

    @pytest.mark.system
    def test_search_by_name_and_zap2it_and_imdb(self):
        with pytest.raises(HTTPError):
            assert not TVDB().search().series(name='Doctor Who', zap2it_id='EP00750178', imdb_id='tt0436992')

    @pytest.mark.system
    def test_search_with_version(self):
        res = TVDB(version='2.1.1').search().series(name='Doctor Who')
        assert len(res) == 12

    @pytest.mark.system
    def test_search_different_language(self):
        res = TVDB(language='de').search().series(imdb_id='tt0436992')
        assert len(res[0].aliases) == 0
        assert res[0].overview == "Die Serie handelt von einem mysteriösen Außerirdischen namens „Der Doktor“, der " \
                                  "mit seinem Raumschiff, der TARDIS (Time and Relative Dimension in Space), welches" \
                                  " von außen aussieht wie eine englische Notruf-Telefonzelle der 60er Jahre, durch" \
                                  " Raum und Zeit fliegt. Der Doktor ist ein Time Lord vom Planeten Gallifrey - und" \
                                  " bereits über 900 Jahre alt. Dass man ihm das nicht ansieht, liegt vor allem" \
                                  " daran, dass ein Time Lord, wenn er stirbt, in der Lage ist, sich zu regenerieren," \
                                  " wobei er auch eine andere Gestalt annimmt."


class TestSeries:
    @pytest.mark.system
    def test_get_series_by_id(self):
        res = TVDB().series(76107)
        assert res.series_name == "Doctor Who"


class TestSeriesActors:
    @pytest.mark.system
    def test_get_series_actors(self):
        res = TVDB().series(76107).actors()
        assert len(res) == 42


class TestSeriesEpisodes:
    @pytest.mark.system
    def test_single_page(self):
        res = TVDB().series(78874).episodes()
        assert len(res) == 18

    @pytest.mark.system
    def test_many_pages(self):
        res = TVDB().series(76107).episodes()
        assert len(res) == 809

    @pytest.mark.system
    def test_summary(self):
        res = TVDB().series(76107).episodes().summary()
        assert len(res.aired_seasons) == 27
        assert res.aired_episodes == 809
        assert res.dvd_seasons == []
        assert res.dvd_episodes == 0


class TestEpisodes:
    @pytest.mark.system
    def test_get_episode(self):
        res = TVDB().episodes(183284)
        assert res.episode_name == 'Terror of the Zygons (2)'
        assert res.directors == ['Douglas Camfield']
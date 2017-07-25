import datetime

import pytest

from pytvdb.models import SeriesData, SeriesSearchData, SeriesActorsData, BasicEpisode, SeriesEpisodes, BaseModel, \
    SeriesEpisodesSummary


class TestModels:
    @pytest.mark.unit
    def test_search_series_data(self):
        data = {
            "aliases": [
                  "Doctor Who (1963)",
                  "Dr Who"
                ],
            "banner": "graphical/76107-g14.jpg",
            "firstAired": "1963-11-23",
            "id": 76107,
            "network": "BBC One",
            "overview": "Doctor Who is the longest-running science fiction TV series in history, airing initially from "
                        "1963 to 1989. Doctor Who is about ideas. It pioneered sophisticated mixed-level storytelling. "
                        "Its format was the key to its longevity: the Doctor, a mysterious traveller in space and time,"
                        " travels in his ship, the TARDIS. The TARDIS can take him and his companions anywhere in time"
                        " and space. Inevitably he finds evil at work wherever he goes...",
            "seriesName": "Doctor Who",
            "status": "Ended"
        }
        s = SeriesSearchData(**data)
        assert len(s.aliases) == 2
        assert s.banner == data['banner']
        assert s.first_aired == datetime.date(1963, 11, 23)
        assert s.id == data['id']
        assert s.network == data['network']
        assert s.overview == data['overview']
        assert s.series_name == data['seriesName']
        assert s.status == data['status']

    @pytest.mark.unit
    def test_series_data(self):
        data = {
            "id": 76107,
            "seriesName": "Doctor Who",
            "aliases": [
                "Doctor Who (1963)",
                "Dr Who"
            ],
            "banner": "graphical/76107-g14.jpg",
            "seriesId": "355",
            "status": "Ended",
            "firstAired": "1963-11-23",
            "network": "BBC One",
            "networkId": "GJ8dPeHC",
            "runtime": "25",
            "genre": [
                "Action",
                "Adventure",
                "Science-Fiction"
            ],
            "overview": "Doctor Who is the longest-running science fiction TV series in history, airing initially from"
                        " 1963 to 1989.  Doctor Who is about ideas.  It pioneered sophisticated mixed-level"
                        " storytelling. Its format was the key to its longevity: the Doctor, a mysterious traveller in"
                        " space and time, travels in his ship, the TARDIS.  The TARDIS can take him and his companions"
                        " anywhere in time and space. Inevitably he finds evil at work wherever he goes...",
            "lastUpdated": 1500845512,
            "airsDayOfWeek": "Saturday",
            "airsTime": "5:15 PM",
            "rating": "TV-PG",
            "imdbId": "tt0056751",
            "zap2itId": "EP001301",
            "added": "2014-05-13 07:21:40",
            "siteRating": 9.4,
            "siteRatingCount": 177
        }
        s = SeriesData(**data)
        assert isinstance(s, SeriesSearchData)
        assert s.added == datetime.datetime(2014, 5, 13, 7, 21, 40)
        assert s.airs_day_of_week == data['airsDayOfWeek']
        assert s.airs_time == data['airsTime']
        assert len(s.genre) == len(data['genre'])
        assert s.imdb_id == data['imdbId']
        assert int(s.last_updated.timestamp()) == data['lastUpdated']
        assert s.network_id == data['networkId']
        assert s.rating == data['rating']
        assert s.runtime == data['runtime']
        assert s.series_id == int(data['seriesId'])
        assert s.site_rating == data['siteRating']
        assert s.site_rating_count == data['siteRatingCount']
        assert s.zap2it_id == data['zap2itId']

    @pytest.mark.unit
    def test_series_actor_data(self):
        data = {
            "id": 43198,
            "seriesId": 76107,
            "name": "Sarah Sutton",
            "role": "Nyssa",
            "sortOrder": 3,
            "image": "actors/43198.jpg",
            "imageAuthor": 7570,
            "imageAdded": "2009-01-12 17:45:32",
            "lastUpdated": "2009-01-12 17:45:32"
        }
        a = SeriesActorsData(**data)
        assert a.id == data['id']
        assert a.series_id == data['seriesId']
        assert a.name == data['name']
        assert a.role == data['role']
        assert a.sort_order == data['sortOrder']
        assert a.image == data['image']
        assert a.image_author == data['imageAuthor']
        assert a.image_added.strftime('%Y-%m-%d %H:%M:%S') == data['imageAdded']
        assert a.last_updated.strftime('%Y-%m-%d %H:%M:%S') == data['lastUpdated']

    @pytest.mark.unit
    def test_basic_episode(self):
        data = {
            "absoluteNumber": None,
            "airedEpisodeNumber": 1,
            "airedSeason": 1,
            "airedSeasonID": 9666,
            "dvdEpisodeNumber": None,
            "dvdSeason": None,
            "episodeName": "An Unearthly Child (1)",
            "firstAired": "1963-11-23",
            "id": 183204,
            "lastUpdated": 1462622449,
            "overview": "London, 1963. Schoolteachers Ian Chesterton and Barbara Wright are perplexed by the behaviour"
                        " of one of their pupils, Susan Foreman. Her knowledge of science and history exceeds theirs,"
                        " yet she seems totally ignorant of many common aspects of everyday life. They follow her to"
                        " her home address, a junkyard with a police telephone box standing in it, and encounter her"
                        " grandfather, the enigmatic Doctor. When they force their way past him into the police box,"
                        " Susan's secret is revealed: she and the Doctor are aliens, and the police box is a time"
                        " machine, the TARDIS, capable of visiting any point in the universe at any moment in time…"
        }
        e = BasicEpisode(**data)
        assert e.absolute_number == data['absoluteNumber']
        assert e.aired_episode_number == data['airedEpisodeNumber']
        assert e.aired_season == data['airedSeason']
        assert e.dvd_episode_number == data['dvdEpisodeNumber']
        assert e.dvd_season == data['dvdSeason']
        assert e.episode_name == data['episodeName']
        assert e.first_aired.strftime('%Y-%m-%d') == data['firstAired']
        assert e.id == data['id']
        assert int(e.last_updated.timestamp()) == data['lastUpdated']
        assert e.overview == data['overview']

    @pytest.mark.unit
    def test_series_episodes(self):
        data = [1,2,3,4,5]
        e = SeriesEpisodes(data)
        assert len(e) == 5
        for i in range(0, 5):
            assert e[i] == data[i]

        assert 3 in e
        for i, ep in zip(data, e):
            assert i == ep

        for i, ep in zip(reversed(data), reversed(e)):
            assert i == ep

    @pytest.mark.unit
    def test_series_episodes_summary(self):
        data = {
            "airedSeasons": [
                "21",
                "20",
                "19",
                "0",
                "18",
                "26",
                "25",
                "24",
                "22",
                "23",
                "14",
                "13",
                "12",
                "11",
                "17",
                "16",
                "15",
                "9",
                "3",
                "5",
                "6",
                "10",
                "8",
                "2",
                "1",
                "7",
                "4"
            ],
            "airedEpisodes": "809",
            "dvdSeasons": [],
            "dvdEpisodes": "0"
        }
        s = SeriesEpisodesSummary(**data)
        assert len(s.aired_seasons) == 27
        assert s.aired_episodes == 809
        assert s.dvd_seasons == []
        assert s.dvd_episodes == 0


class TestBaseModel:
    @pytest.mark.unit
    @pytest.mark.parametrize("input,func, expected", [
        ([], lambda l: l + [1], []),
        ([1], lambda l: l + [1], [1, 1]),
        ('', lambda l: l + '1', None),
        ('1', lambda l: l + '1', '11'),
        ('0', lambda l: l + '1', '01'),
        (0, lambda l: l + 1, 1),
        (1, lambda l: l + 1, 2)
    ])
    def test_apply_func_or_none(self, input, func, expected):
        res = BaseModel._apply_func_or_none(func, input)
        assert res == expected


class TestSeriesEpisodeQuery:

    @pytest.fixture(scope='session')
    def data(self):
        data = [
            {
                "absoluteNumber": 2,
                "airedEpisodeNumber": 1,
                "airedSeason": 1,
                "airedSeasonID": 15791,
                "dvdEpisodeNumber": 2,
                "dvdSeason": 1,
                "episodeName": "The Train Job",
                "firstAired": "2002-09-20",
                "id": 297989,
                "language": {
                    "episodeName": "en",
                    "overview": "en"
                },
                "lastUpdated": 1458047554,
            },{
                "absoluteNumber": 15,
                "airedEpisodeNumber": 1,
                "airedSeason": 0,
                "airedSeasonID": 26328,
                "dvdEpisodeNumber": None,
                "dvdSeason": None,
                "episodeName": "Serenity",
                "firstAired": "2005-09-30",
                "id": 415679,
                "language": {
                    "episodeName": "en",
                    "overview": "en"
                },
                "lastUpdated": 1358950216,
            },{
                "absoluteNumber": 3,
                "airedEpisodeNumber": 2,
                "airedSeason": 1,
                "airedSeasonID": 15791,
                "dvdEpisodeNumber": 3,
                "dvdSeason": 1,
                "episodeName": "Bushwhacked",
                "firstAired": "2002-09-27",
                "id": 297990,
                "language": {
                    "episodeName": "en",
                    "overview": "en"
                },
                "lastUpdated": 1458047574,
            },{
                "absoluteNumber": None,
                "airedEpisodeNumber": 2,
                "airedSeason": 0,
                "airedSeasonID": 26328,
                "dvdEpisodeNumber": None,
                "dvdSeason": None,
                "episodeName": "Here’s How It Was: The Making of “Firefly”",
                "firstAired": "2003-12-09",
                "id": 1000141,
                "language": {
                    "episodeName": "en",
                    "overview": "en"
                },
                "lastUpdated": 1465738872,
            },{
                "absoluteNumber": 6,
                "airedEpisodeNumber": 3,
                "airedSeason": 1,
                "airedSeasonID": 15791,
                "dvdEpisodeNumber": 6,
                "dvdSeason": 1,
                "episodeName": "Our Mrs. Reynolds",
                "firstAired": "2002-10-04",
                "id": 297991,
                "language": {
                    "episodeName": "en",
                    "overview": "en"
                },
                "lastUpdated": 1458047585,
            },{
                "absoluteNumber": None,
                "airedEpisodeNumber": 3,
                "airedSeason": 0,
                "airedSeasonID": 26328,
                "dvdEpisodeNumber": None,
                "dvdSeason": None,
                "episodeName": "Done the Impossible",
                "firstAired": "2006-07-28",
                "id": 967981,
                "language": {
                    "episodeName": "en",
                    "overview": "en"
                },
                "lastUpdated": 1270848353,
            },{
                "absoluteNumber": 7,
                "airedEpisodeNumber": 4,
                "airedSeason": 1,
                "airedSeasonID": 15791,
                "dvdEpisodeNumber": 7,
                "dvdSeason": 1,
                "episodeName": "Jaynestown",
                "firstAired": "2002-10-18",
                "id": 297992,
                "language": {
                    "episodeName": "en",
                    "overview": "en"
                },
                "lastUpdated": 1458047594,
            },{
                "absoluteNumber": None,
                "airedEpisodeNumber": 4,
                "airedSeason": 0,
                "airedSeasonID": 26328,
                "dvdEpisodeNumber": None,
                "dvdSeason": None,
                "episodeName": "Browncoats Unite",
                "firstAired": "2012-11-11",
                "id": 4360465,
                "language": {
                    "episodeName": "en",
                    "overview": "en"
                },
                "lastUpdated": 1353371788,
            },{
                "absoluteNumber": 8,
                "airedEpisodeNumber": 5,
                "airedSeason": 1,
                "airedSeasonID": 15791,
                "dvdEpisodeNumber": 8,
                "dvdSeason": 1,
                "episodeName": "Out of Gas",
                "firstAired": "2002-10-25",
                "id": 297993,
                "language": {
                    "episodeName": "en",
                    "overview": "en"
                },
                "lastUpdated": 1458047604,
            },{
                "absoluteNumber": 4,
                "airedEpisodeNumber": 6,
                "airedSeason": 1,
                "airedSeasonID": 15791,
                "dvdEpisodeNumber": 4,
                "dvdSeason": 1,
                "episodeName": "Shindig",
                "firstAired": "2002-11-01",
                "id": 297994,
                "language": {
                    "episodeName": "en",
                    "overview": "en"
                },
                "lastUpdated": 1458047612,
            },{
                "absoluteNumber": 5,
                "airedEpisodeNumber": 7,
                "airedSeason": 1,
                "airedSeasonID": 15791,
                "dvdEpisodeNumber": 5,
                "dvdSeason": 1,
                "episodeName": "Safe",
                "firstAired": "2002-11-08",
                "id": 297995,
                "language": {
                    "episodeName": "en",
                    "overview": "en"
                },
                "lastUpdated": 1458047620,
            },{
                "absoluteNumber": 9,
                "airedEpisodeNumber": 8,
                "airedSeason": 1,
                "airedSeasonID": 15791,
                "dvdEpisodeNumber": 9,
                "dvdSeason": 1,
                "episodeName": "Ariel",
                "firstAired": "2002-11-15",
                "id": 297996,
                "language": {
                    "episodeName": "en",
                    "overview": "en"
                },
                "lastUpdated": 1458047631,
            },{
                "absoluteNumber": 10,
                "airedEpisodeNumber": 9,
                "airedSeason": 1,
                "airedSeasonID": 15791,
                "dvdEpisodeNumber": 10,
                "dvdSeason": 1,
                "episodeName": "War Stories",
                "firstAired": "2002-12-06",
                "id": 297997,
                "language": {
                    "episodeName": "en",
                    "overview": "en"
                },
                "lastUpdated": 1458047638,
            },{
                "absoluteNumber": 14,
                "airedEpisodeNumber": 10,
                "airedSeason": 1,
                "airedSeasonID": 15791,
                "dvdEpisodeNumber": 14,
                "dvdSeason": 1,
                "episodeName": "Objects in Space",
                "firstAired": "2002-12-13",
                "id": 297998,
                "language": {
                    "episodeName": "en",
                    "overview": "en"
                },
                "lastUpdated": 1458047646,
            },{
                "absoluteNumber": 1,
                "airedEpisodeNumber": 11,
                "airedSeason": 1,
                "airedSeasonID": 15791,
                "dvdEpisodeNumber": 1,
                "dvdSeason": 1,
                "episodeName": "Serenity",
                "firstAired": "2002-12-20",
                "id": 297999,
                "language": {
                    "episodeName": "en",
                    "overview": "en"
                },
                "lastUpdated": 1458047658,
            },{
                "absoluteNumber": 13,
                "airedEpisodeNumber": 12,
                "airedSeason": 1,
                "airedSeasonID": 15791,
                "dvdEpisodeNumber": 13,
                "dvdSeason": 1,
                "episodeName": "Heart of Gold",
                "firstAired": "2003-06-23",
                "id": 298001,
                "language": {
                    "episodeName": "en",
                    "overview": "en"
                },
                "lastUpdated": 1458047667,
            },{
                "absoluteNumber": 11,
                "airedEpisodeNumber": 13,
                "airedSeason": 1,
                "airedSeasonID": 15791,
                "dvdEpisodeNumber": 11,
                "dvdSeason": 1,
                "episodeName": "Trash",
                "firstAired": "2003-07-21",
                "id": 298002,
                "language": {
                    "episodeName": "en",
                    "overview": "en"
                },
                "lastUpdated": 1458047676,
            },{
                "absoluteNumber": 12,
                "airedEpisodeNumber": 14,
                "airedSeason": 1,
                "airedSeasonID": 15791,
                "dvdEpisodeNumber": 12,
                "dvdSeason": 1,
                "episodeName": "The Message",
                "firstAired": "2003-07-28",
                "id": 298003,
                "language": {
                    "episodeName": "en",
                    "overview": "en"
                },
                "lastUpdated": 1458047683,
            }
        ]
        return SeriesEpisodes([BasicEpisode(**d) for d in data])

    @pytest.mark.unit
    def test_query_by_absolute_number(self, data):
        res = data.query(absolute_number=2)
        assert len(res) == 1
        assert res[0].episode_name == 'The Train Job'

    @pytest.mark.unit
    def test_query_by_aired_season(self, data):
        res = data.query(aired_season=0)
        assert len(res) == 4

    @pytest.mark.unit
    def test_query_by_aired_episode(self, data):
        res = data.query(aired_episode=5)
        assert len(res) == 1
        assert res[0].episode_name == 'Out of Gas'

    @pytest.mark.unit
    def test_query_by_dvd_season(self, data):
        res = data.query(dvd_season=1)
        assert len(res) == 14

    @pytest.mark.unit
    def test_query_by_dvd_episode(self, data):
        res = data.query(dvd_episode=1)
        assert len(res) == 1
        assert res[0].episode_name == 'Serenity'

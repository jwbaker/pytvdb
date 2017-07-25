import datetime

from pytvdb.models import SeriesData, SeriesSearchData, SeriesActorsData, BasicEpisode


class TestUnitModels:
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
from pytvdb.models import Series


class TestUnitSeriesModel:
    def test_fields_set(self):
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
        s = Series(**data)
        assert len(s.aliases) == 2
        assert s.banner == data['banner']
        assert s.firstAired == data['firstAired']
        assert s.id == data['id']
        assert s.network == data['network']
        assert s.overview == data['overview']
        assert s.seriesName == data['seriesName']
        assert s.status == data['status']
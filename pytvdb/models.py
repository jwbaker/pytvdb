from datetime import date

__all__ = ['Series']


class BaseModel:
    def __init__(self, fields, **kwargs):
        self._attrs = {f:self.__class__._apply_func_or_none(transform, kwargs.get(f))
                       for f, transform in fields.items() if f in kwargs}

    @staticmethod
    def _apply_func_or_none(func, arg):
        if isinstance(arg, list):
            return func(arg) if arg else []
        return func(arg) if arg else None


class Series(BaseModel):
    def __init__(self, **kwargs):
        super(Series, self).__init__({
            'aliases': list,
            'banner': str,
            'firstAired': lambda s: date(*map(int, s.split('-'))),
            'id': int,
            'network': str,
            'overview': str,
            'seriesName': str,
            'status': str
        }, **kwargs)

    @property
    def aliases(self):
        return self._attrs.get('aliases')

    @property
    def banner(self):
        return self._attrs.get('banner')

    @property
    def first_aired(self):
        return self._attrs.get('firstAired')

    @property
    def id(self):
        return self._attrs.get('id')

    @property
    def network(self):
        return self._attrs.get('network')

    @property
    def overview(self):
        return self._attrs.get('overview')

    @property
    def series_name(self):
        return self._attrs.get('seriesName')

    @property
    def status(self):
        return self._attrs.get('status')
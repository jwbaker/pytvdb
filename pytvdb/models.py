from datetime import date

__all__ = ['Series']


class BaseModel:
    def __init__(self, fields, **kwargs):
        self._attrs = {f:self.__class__._apply_func_or_none(transform, kwargs.get(f))
                       for f, transform in fields.items() if f in kwargs}

    def __getattr__(self, item):
        try:
            return self._attrs[item]
        except KeyError as ex:
            raise AttributeError from ex

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
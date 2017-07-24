__all__ = ['Series']


class BaseModel:
    def __init__(self, fields, **kwargs):
        self._attrs = {f:kwargs.get(f, None) for f in fields}

    def __getattr__(self, item):
        try:
            return self._attrs[item]
        except KeyError as ex:
            raise AttributeError from ex


class Series(BaseModel):
    def __init__(self, **kwargs):
        super(Series, self).__init__([
            'aliases',
            'banner',
            'firstAired',
            'id',
            'network',
            'overview',
            'seriesName',
            'status'
        ], **kwargs)
__all__ = ['Series']

class BaseModel:
    def __init__(self, fields, **kwargs):
        self._attrs = {f:kwargs.get(f, None) for f in fields}

    def __getattr__(self, item):
        return self._attrs[item]


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
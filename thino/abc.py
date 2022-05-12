
from typing import Any, Dict


class BaseObject:

    __slots__ = (
        "status",
        "url",
        "response",
    )

    def __init__(self, response: Dict[str, Any], type: str) -> None:
        self.response = response
        tmp = self.__slots__
        self.__class__.__name__ = type.capitalize()
        keys = {k: v for k, v in response.items() if k in tmp}
        for k, v in keys.items():
            setattr(self, k, v)
            continue

    def __repr__(self) -> str:
        return f"<{self.__class__.__name__} url: {self.url!r}, status: {self.status}>"

    @property
    def raw(self) -> Dict[str, Any]:
        return self.response


class SearchObject:
    __slots__ = (
        'response',
        'filename',
        'image',
        'status',
        'url',
        'type',
    )

    def __init__(self, response: Dict[str, Any], type: str) -> None:
        self.response = response
        tmp = self.__slots__
        self.__class__.__name__ =  self.type = type.capitalize()
        keys = {k: v for k, v in response.items() if k in tmp}
        for k, v in keys.items():
            setattr(self, k, v)

    def __repr__(self) -> str:
        return f"<{self.__class__.__name__} url: {self.url!r}, filename: {self.filename!r}, status: {self.status} type: {self.type!r}>"

    @property
    def raw(self) -> Dict[str, Any]:
        return self.response
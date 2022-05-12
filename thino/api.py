import urllib

from thino.abc import BaseObject, SearchObject


from . import http, dict, errors

noresponse = "Couldn't contact the API right now..."

class Client:
    def __init__(self):
        pass

    async def tomboy(self) -> BaseObject:
        return await http.get("tomboy")

    async def femboy(self) -> BaseObject:
        return await http.get("femboy")

    async def search(self, target: str) -> SearchObject:
        return await http.search(target)

    async def close(self) -> None:
        await http.close()
    




async def status(target: str):

    if target is None:
        raise errors.EmptyArgument(
            "You have to at least define an argument in string format"
            )

    if not target.lower():
        raise errors.InvalidArgument(
            "You haven't added any valid arguments!"
        )

    try:
        r = await http.status(target.lower())
    except Exception:
        raise errors.NothingFound(noresponse)


    return r



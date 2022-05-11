import urllib


from . import http, dict, errors

noresponse = "Couldn't contact the API right now..."

async def img(target: str):
    possible = [
        "tomboy",
    ]

    if target is None:
        raise errors.EmptyArgument(
            "You have to at least define an argument in string format\nArguments: {}".format(
                possible
            )
        )

    if target.lower() not in possible:
        raise errors.InvalidArgument(
            "You haven't added any valid arguments\nArguments: {}".format(possible)
        )

    try:
        r = await http.get(target.lower())
    except Exception:
        raise errors.NothingFound(noresponse)

    return await r["url"]
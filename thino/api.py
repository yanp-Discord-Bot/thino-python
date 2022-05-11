import urllib


from . import http, dict, errors

noresponse = "Couldn't contact the API right now..."

async def img(target: str, **kwargs):
    possible = [
        "tomboy",
        "helltaker",
        "femboy",
        "neko",
        "hentai",
        "dildo",
        "porn",
        "thighs"
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

    endpoint = r["endpoint"]
    url = r["url"]

    return r



async def search(target: str):

    if target is None:
        raise errors.EmptyArgument(
            "You have to at least define an argument in string format"
            )

    if not target.lower():
        raise errors.InvalidArgument(
            "You haven't added any valid arguments!"
        )

    try:
        r = await http.search(target.lower())
    except Exception:
        raise errors.NothingFound(noresponse)

    endpoint = r["url"]
    filename = r["filename"]
    url = r["image"]

    return r

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

import urllib


from . import http, dict, errors

noresponse = "Couldn't contact the API right now..."

def img(target: str):
    possible = [
        "tomboy",
        "helltaker"
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
        r = http.get(target.lower())
    except Exception:
        raise errors.NothingFound(noresponse)

    endpoint = r["endpoint"]
    url = r["url"]

    return f"{url}\n{endpoint}"
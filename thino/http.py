import aiohttp

class RequestsApi:
    def __init__(self, base_url: str, **kwargs):
        self.base_url = base_url
        self.session = aiohttp.ClientSession()
        for arg in kwargs:
            if isinstance(kwargs[arg], dict):
                kwargs[arg] = self.__deep_merge(getattr(self.session, arg), kwargs[arg])
            setattr(self.session, arg, kwargs[arg])

    async def get(self, url, **kwargs):
        """
       
        uses GET to get json data or any other data from a specified URL endpoint
        Parameters
        ----------
        url: :class:`str`
            The URL endpoint to get data from.
        """
        return await self.session.get(self.base_url + url, **kwargs)

    async def post(self, url, **kwargs):
        return await self.session.post(self.base_url + url, **kwargs)


    @staticmethod
    def __deep_merge(source, destination):
        for key, value in source.items():
            if isinstance(value, dict):
                node = destination.setdefault(key, {})
                RequestsApi.__deep_merge(value, node)
            else:
                destination[key] = value
        return destination


BASEURL = RequestsApi("https://thino.pics/api/v1")


async def get(endpoint):
    r = BASEURL.get(endpoint)

    return r.json()

    
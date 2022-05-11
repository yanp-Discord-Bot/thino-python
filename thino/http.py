import aiohttp

import asyncio

class RequestsApi:
    def __init__(self, base_url: str, loop=None, **kwargs):
        self.loop = asyncio.get_event_loop() if loop is None else loop
        self.base_url = base_url
        self.session = aiohttp.ClientSession(loop=self.loop)
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

    def _run(self, future):
        return self.loop.run_until_complete(future)

    async def __aexit__(self, *error_details): 
    # await but don't return, if exit returns truethy value it suppresses exceptions.
        await self.run(self.session.close())
    async def __aenter__(self):
        return self

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

    
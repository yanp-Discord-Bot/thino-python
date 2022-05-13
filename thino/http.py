from typing import Optional
import aiohttp
import platform
from .abc import BaseObject, SearchObject
import thino.errors 

__version__ = "0.0.1"

class RequestsApi:
    def __init__(self, base_url, **kwargs):
        self.base_url = base_url
        self.session = None
        self.started = False
        self.ENDPOINTS = ["tomboy", "neko", "femboy", "porn", "hentai", "thighs", "helltaker"]
        for arg in kwargs:
            if isinstance(kwargs[arg], dict):
                kwargs[arg] = self.__deep_merge(getattr(self.session, arg), kwargs[arg])
            setattr(self.session, arg, kwargs[arg])

    async def _get(self, endpoint: Optional[str], **kwargs):
        if self.started == False:
            await self.start()
            self.started = True
        
        if endpoint not in self.ENDPOINTS:
            raise ValueError(f"{endpoint} is not a valid endpoint. \nPlease use a endpoint specified here: {self.ENDPOINTS}")

        async with self.session.get(f"{self.base_url}/{endpoint}") as resp:
            return BaseObject(await resp.json(), endpoint)

    async def _search(self, filename: Optional[str]):
        if self.started == False:
            await self.start()
            self.started = True

        if filename is None:
            return "Please specify a filename"

        async with self.session.get(f"{self.base_url}/{filename}") as response:
            return SearchObject(await response.json(), filename)



    async def _post(self, url, **kwargs):
        return await self.session.post(self.base_url + url, **kwargs)

    async def _status(self, endpoint: Optional[str], **kwargs):
        if self.started == False:
            await self.start()
            self.started = True
    

        if endpoint is None:
            return thino.errors.EmptyArgument("Please insert an endpoint!")
    

        async with self.session.get(f"{self.base_url}/{endpoint}") as resp:
            return resp.status

        

    async def start(self):
        self.session = aiohttp.ClientSession( headers={
            "User-Agent": f"Thino-Client @ {__version__}/ Python/{platform.python_version()}/ aiohttp/{aiohttp.__version__}"
        })

    
    async def close(self) -> None:
        await self.session.close() #type: ignore

    @staticmethod
    def __deep_merge(source, destination):
        for key, value in source.items():
            if isinstance(value, dict):
                node = destination.setdefault(key, {})
                RequestsApi.__deep_merge(value, node)
            else:
                destination[key] = value
        return destination




baseurl = RequestsApi("https://thino.pics/api/v1/")
searchurl = RequestsApi("https://thino.pics/search/")



async def get(endpoint):
    return await baseurl._get(endpoint)


async def search(query: str) -> SearchObject:
    return await searchurl._search(query)

async def status(endpoint: str):
    return await baseurl._status(endpoint)

async def close() -> None:
    await baseurl.session.close() #type: ignore
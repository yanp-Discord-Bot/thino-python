import requests


class RequestsApi:
    def __init__(self, base_url, **kwargs):
        self.base_url = base_url
        self.session = requests.Session()
        for arg in kwargs:
            if isinstance(kwargs[arg], dict):
                kwargs[arg] = self.__deep_merge(getattr(self.session, arg), kwargs[arg])
            setattr(self.session, arg, kwargs[arg])

    async def get(self, url, **kwargs):
        return self.session.get(self.base_url + url, **kwargs)

    async def post(self, url, **kwargs):
        return self.session.post(self.base_url + url, **kwargs)

    async def status(self, url, **kwargs):
        resp = self.session.get(url)
        return resp.status_code
    
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
    r = await baseurl.get(endpoint)
    return r.json()

async def search(filename):
    r = await searchurl.get(filename)
    return r.json()

async def status():
    r = await baseurl.status()
    return r
from __future__ import annotations
from types import SimpleNamespace
from typing import Any, Dict, NamedTuple, Optional, Type, Tuple, Union, List
from typing_extensions import TypeAlias
from datetime import datetime   
import aiohttp
from thino import urls
import platform
from . import __version__


__all__ = Tuple[str, ...] = (
    'http'
)


class Rates(NamedTuple):
    remaining: str
    used: str
    total: str
    reset_when: Union[datetime, str]
    last_request: Union[datetime, str]


# aiohttp request tracking / checking bits
async def on_req_start(
    session: aiohttp.ClientSession, ctx: SimpleNamespace, params: aiohttp.TraceRequestStartParams
) -> None:
    """Before-request hook to make sure we don't overrun the ratelimit."""
    # print(repr(session), repr(ctx), repr(params))
    pass


async def on_req_end(session: aiohttp.ClientSession, ctx: SimpleNamespace, params: aiohttp.TraceRequestEndParams) -> None:
    """After-request hook to adjust remaining requests on this time frame."""
    headers = params.response.headers

    remaining = headers['X-RateLimit-Remaining']
    used = headers['X-RateLimit-Used']
    total = headers['X-RateLimit-Limit']
    reset_when = datetime.fromtimestamp(int(headers['X-RateLimit-Reset']))
    last_req = datetime.utcnow()

    session._rates = Rates(remaining, used, total, reset_when, last_req)


trace_config = aiohttp.TraceConfig()
trace_config.on_request_start.append(on_req_start)
trace_config.on_request_end.append(on_req_end)

class http:
    def __init__(self, headers: Dict[str, Union[str, int]], auth: Union[aiohttp.BasicAuth, None]) -> None:
        if not headers.get('User-Agent'):
            headers[
                'User-Agent'
            ] = f'Github-API-Wrapper (https://github.com/VarMonke/Github-Api-Wrapper) @ {__version__} Python/{platform.python_version()} aiohttp/{aiohttp.__version__}'

        self._rates = Rates('', '', '', '', '')
        self.headers = headers
        self.auth = auth
    def __await__(self):
        return self.start().__await__()


    async def start(self):
        self.session = aiohttp.ClientSession(
            headers=self.headers,  # type: ignore
            auth=self.auth,
            trace_configs=[trace_config],
        )
        if not hasattr(self.session, "_rates"):
            self.session._rates = Rates('', '', '', '', '')
        return self


    async def get_user(self, username: str) -> Dict[str, Union[str, int]]:
        """Returns a user's public data in JSON format."""
        result = await self.session.get(urls.TOMBOY_URL)
        if 200 <= result.status <= 299:
            return await result.json()
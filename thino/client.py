from __future__ import annotations
import aiohttp
from typing import (
    Tuple
)

from .urls import *

__all__: Tuple[str, ...] = ('API',)

class API:
    def __init__(self):
        self.url = "https://thino.pics/api/v1/tomboy"

    def get(self):
        response = requests.get(self.url)
        return response.text
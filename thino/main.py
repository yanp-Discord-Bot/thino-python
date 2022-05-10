from __future__ import annotations
import requests
from typing import (
    Tuple
)

__all__: Tuple[str, ...] = ('API',)

class API:
    def __init__(self):
        self.url = "https://thino.pics/api/v1"

    def get(self,route:str=None):
        response = requests.get(self.url +route)
        return response.status_code
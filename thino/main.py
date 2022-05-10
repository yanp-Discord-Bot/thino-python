from __future__ import annotations
import requests
from typing import (
    Tuple
)

__all__: Tuple[str, ...] = ('API',)

class API:
    def __init__(self):
        self.url = "https://thino.pics/api/v1/tomboy"

    def get(self):
        response = requests.get(self.url)
        return response.text
from typing import Any
import requests
import json

from config import BRMS_URL


def get_API_data(date: str) -> dict[Any, Any]:
    url_with_date = f"{BRMS_URL}/{date}"
    response = requests.get(url_with_date)
    data = response.json()
    print("***data", data)
    return {}

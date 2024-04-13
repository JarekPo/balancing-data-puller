from typing import Any
import requests

from config import BRMS_URL


def get_api_data(date: str) -> Any:
    url_with_date = f"{BRMS_URL}/{date}"
    response = requests.get(url_with_date)
    data = response.json()
    return data

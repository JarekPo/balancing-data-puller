from typing import Any
import requests

from config import BRMS_URL


def get_api_data(date: str) -> Any:
    print("BRMS_URL:", BRMS_URL)
    url_with_date = f"{BRMS_URL}/{date}"
    print("url_with_date", url_with_date)
    response = requests.get(url_with_date)
    data = response.json()
    print("***data", data)
    return data

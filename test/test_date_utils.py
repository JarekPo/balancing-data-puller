import pytest
from utils.date_utils import get_date_range
from freezegun import freeze_time
from datetime import datetime


@freeze_time("2024-04-18")
def test_date_utils() -> None:

    assert get_date_range(5) == [
        "2024-04-18",
        "2024-04-17",
        "2024-04-16",
        "2024-04-15",
        "2024-04-14",
    ]

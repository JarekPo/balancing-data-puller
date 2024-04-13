from datetime import datetime, timedelta
from typing import List


def get_date_range(number_of_days: int) -> List[str]:
    current_date = datetime.today()

    dates: List[str] = []
    dates.append(current_date.date().strftime("%Y-%m-%d"))
    for day in range(number_of_days - 1):
        date = current_date - timedelta(days=day + 1)
        dates.append(date.date().strftime("%Y-%m-%d"))

    return dates

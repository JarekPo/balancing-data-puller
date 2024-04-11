import datetime
from api_requests.api_requests import get_API_data

current_date = datetime.datetime.today().strftime("%Y-%m-%d")
get_API_data(current_date)

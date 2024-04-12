import datetime
from api_requests.api_requests import get_API_data
from database.database import create_brms_table, insert_data_to_db

current_date = datetime.datetime.today().strftime("%Y-%m-%d")
date = "2024-04-10"

create_brms_table()
insert_data_to_db(get_API_data(date))

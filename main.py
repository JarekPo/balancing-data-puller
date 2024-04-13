import datetime
from database.database import (
    create_brms_table,
)
from utils.data_handler import handle_received_data

current_date = datetime.datetime.today().strftime("%Y-%m-%d")
date = "2024-04-08"

create_brms_table()
handle_received_data(date)

from database.database import (
    create_brms_table,
)
from utils.data_handler import handle_received_data
from utils.date_utils import get_date_range

NUMBER_OF_DAYS_TO_PULL = 2

create_brms_table()

dates = get_date_range(NUMBER_OF_DAYS_TO_PULL)
for date in dates:
    handle_received_data(date)

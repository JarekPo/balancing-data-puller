import time
from database.database import (
    create_brms_table,
)
from utils.cron_manager import set_cron_job
from utils.data_handler import handle_received_data
from utils.date_utils import get_date_range


NUMBER_OF_DAYS_TO_PULL = 2


def main() -> None:
    create_brms_table()

    dates = get_date_range(NUMBER_OF_DAYS_TO_PULL)
    for date in dates:
        handle_received_data(date)

    set_cron_job()

    while True:
        try:
            print("Container running...")
            time.sleep(60)
        except KeyboardInterrupt:
            print("Container stopped")
            break


if __name__ == "__main__":
    main()

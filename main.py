from datetime import datetime
from fcntl import LOCK_EX, LOCK_NB, flock
import logging
import time
from database.database import (
    create_brms_table,
)
from utils.cron_manager import set_cron_job
from utils.data_handler import handle_received_data
from utils.date_utils import get_date_range


NUMBER_OF_DAYS_TO_PULL = 2


def main() -> None:
    now = datetime.now()
    logging.debug("time: " + str(now))

    create_brms_table()

    dates = get_date_range(NUMBER_OF_DAYS_TO_PULL)
    for date in dates:
        handle_received_data(date)

    set_cron_job()


if __name__ == "__main__":
    with open("/app/main.lock", "w") as lockfile:
        try:
            flock(lockfile, LOCK_EX | LOCK_NB)
            main()
        except BlockingIOError:
            logging.debug("Another instance is running, exiting...")

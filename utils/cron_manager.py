import os
from crontab import CronTab
import logging

logging.basicConfig(level=logging.DEBUG)


def set_cron_job() -> None:
    try:
        cron = CronTab(user=True)

        main_script_path = "/app/main.py"

        job = cron.new(command=f"python3 {main_script_path}")

        job.minute.on(0)
        job.minute.every(1)

        cron_file_path = "/root/.crontab.txt"
        cron.write(cron_file_path)

        os.chmod(cron_file_path, 0o600)

        os.system(f"crontab -u root {cron_file_path}")

        logging.debug("****cron executed logging")
        print(cron.render())
        logging.debug(cron.render())

    except Exception as e:
        logging.error(f"An error occurred: {e}")


if __name__ == "__main__":
    set_cron_job()

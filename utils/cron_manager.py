import os
from crontab import CronTab
import logging

logging.basicConfig(level=logging.DEBUG)


def set_cron_job() -> None:
    try:
        cron = CronTab(user=True)
        script_path = os.path.abspath(os.path.dirname(__file__))
        main_script_path = os.path.join(script_path, "..", "main.py")

        job = cron.new(command=f"python3 {main_script_path}")

        job.minute.on(0)
        job.hour.every(1)

        cron_file_path = "/root/.crontab.txt"
        cron.write(cron_file_path)

        os.chmod(cron_file_path, 0o600)

        os.system(f"crontab -u root {cron_file_path}")

        print("**cron executed")

    except Exception as e:
        logging.error(f"An error occurred: {e}")


if __name__ == "__main__":
    set_cron_job()

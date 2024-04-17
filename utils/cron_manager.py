import os
from crontab import CronTab


def set_cron_job() -> None:
    cron = CronTab(user=True)
    script_path = os.path.abspath(os.path.dirname(__file__))
    main_script_path = os.path.join(script_path, "..", "main.py")

    job = cron.new(command=f"python3 {main_script_path}")

    job.minute.on(0)
    job.hour.every(1)

    cron_file_path = "/tmp/crontab.txt"
    cron.write(cron_file_path)

    os.system(f"sudo crontab -u root {cron_file_path}")

    os.remove(cron_file_path)

import subprocess
from crontab import CronTab

# setup and shedule cronjob to receive latest mensa data
USER = "pi"
COMMAND = "python _04_dialog_manager/mensa_parser/mensa_data_requester.py"

crontab_ = CronTab(user = USER)

print("setting up cron job...")

cron_job = crontab_.new(command = COMMAND)
cron_job.day.on(6)
crontab_.write()

print("cronjob successfully set up")

# start main.py
subprocess.run(['python', 'voice_assistant_main.py'])

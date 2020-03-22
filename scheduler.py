import os
from pressreader import job
from apscheduler.triggers.cron import CronTrigger
from apscheduler.schedulers.blocking import BlockingScheduler

cron_schedule = os.environ["CRON_SCHEDULE"]

scheduler = BlockingScheduler()
scheduler.add_job(job, CronTrigger.from_crontab(cron_schedule))

scheduler.start()

from pressreader import job
from apscheduler.triggers.cron import CronTrigger
from apscheduler.schedulers.blocking import BlockingScheduler

cron_schedule = "0 0 */6 * *" # every 6 days
debug_schedule = "*/3 * * * *" # every 3 minutes

scheduler = BlockingScheduler()
scheduler.add_job(job, CronTrigger.from_crontab(debug_schedule))

scheduler.start()

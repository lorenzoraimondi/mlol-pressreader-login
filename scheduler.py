from pressreader import job
from apscheduler.triggers.cron import CronTrigger
from apscheduler.schedulers.blocking import BlockingScheduler

cron_schedule = "0 18 */5 * *" # every 5 days at 6pm
debug_cron_schedule = "*/3 * * * *" # every 3 minutes

scheduler = BlockingScheduler()
scheduler.add_job(job, CronTrigger.from_crontab(cron_schedule))

scheduler.start()

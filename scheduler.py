from pressreader import job
from apscheduler.triggers.cron import CronTrigger
from apscheduler.schedulers.blocking import BlockingScheduler

scheduler = BlockingScheduler()
scheduler.add_job(job, CronTrigger.from_crontab("0 0 */6 * *"))

scheduler.start()

from apscheduler.schedulers.blocking import BlockingScheduler
from apscheduler.triggers.interval import IntervalTrigger
import time 

def task():
    localtime = time.asctime(time.localtime(time.time()))
    print(localtime, ": 執行任務...")
    
scheduler = BlockingScheduler(timezone="Asia/Taipei") 
trigger = IntervalTrigger(seconds=3, timezone="Asia/Taipei")
scheduler.add_job(task, trigger)
try:
    scheduler.start()
except (KeyboardInterrupt, SystemExit):
    scheduler.shutdown() 


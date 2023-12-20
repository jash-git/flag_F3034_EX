from apscheduler.schedulers.blocking import BlockingScheduler
from apscheduler.triggers.interval import IntervalTrigger
import time 

def task(text):
    localtime = time.asctime(time.localtime(time.time()))
    print(localtime, ": 執行任務...", text)
    
scheduler = BlockingScheduler(timezone="Asia/Taipei") 
trigger1 = IntervalTrigger(minutes=1, timezone="Asia/Taipei")
scheduler.add_job(task, trigger1, args=["工作1"])
start_date = '2022-7-1 13:05:00'
end_date = '2022-7-1 13:10:00'
trigger2 = IntervalTrigger(minutes=1, seconds = 30,
                           start_date=start_date,
                           end_date=end_date,
                           timezone="Asia/Taipei")
scheduler.add_job(task, trigger2, args=["工作2"])
try:
    scheduler.start()
except (KeyboardInterrupt, SystemExit):
    scheduler.shutdown() 

from apscheduler.schedulers.blocking import BlockingScheduler
from apscheduler.triggers.date import DateTrigger
import time, datetime 

def task(text):
    localtime = time.asctime(time.localtime(time.time()))
    print(localtime, ": 執行任務...", text)
    
scheduler = BlockingScheduler(timezone="Asia/Taipei") 
run_date = datetime.date(2022,7,1)
trigger1 = DateTrigger(run_date=run_date, timezone="Asia/Taipei")
scheduler.add_job(task, trigger1, args=["工作1"])
run_date = datetime.datetime(2022,7,1,13,0,0)
trigger2 = DateTrigger(run_date=run_date, timezone="Asia/Taipei")
scheduler.add_job(task, trigger2, args=["工作2"])
run_date = "2022-7-1 13:02:00"
trigger3 = DateTrigger(run_date=run_date, timezone="Asia/Taipei")
scheduler.add_job(task, trigger3, args=["工作3"])
try:
    scheduler.start()
except (KeyboardInterrupt, SystemExit):
    scheduler.shutdown() 

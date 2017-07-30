"""
    daily.py: daily tasks management
"""
import timeman as tm
from datetime import datetime

daily_schedule = []
todo_daily_schedule = []

class dailyTask:
    # time: (hour, minute) tuple
    # event: a callable
    def __init__(self, time, event):
        self.time = datetime(year=1970,
            month=1,
            day=1,
            hour=time[0],
            minute=time[1])
        self.event = event
        # automatically append oneself to the list
        daily_schedule.append(self)
    

def daily_task_check():
    # check all the tasks
    today = datetime.now(0)
    while True:
        # refresh list on a new day
        if not tm.at_day(today):
            today = tm.getLocalTime()
            todo_daily_schedule = daily_schedule[:]
        # loop through all to-do tasks
        for task in schedule_list:
            if tm.timeRun(tm.at_tod(task.time),
                task.event):
                todo_daily_schedule.remove(task.event)
        # enough sleep builds better body
        sleep(30)


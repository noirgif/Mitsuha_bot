"""
    timeman: time management
"""
from datetime import datetime
from datetime import timedelta
import pytz
import json

# local timezone
localtz = pytz.timezone(json.load(open('config/misc.json'))["timezone"])


# constants
ten_secs = timedelta(0, 10, 0)
a_day = timedelta(1, 0, 0)
a_week = timedelta(7, 0, 0)
# 5am
time_5am = datetime(year=1970, month=1, day=1, hour=5, minute=0)
# 11pm
time_11pm = datetime(year=1970, month=1, day=1, hour=23, minute=0)

# get local time, in datetime.datetime
def getLocalTime():
    return datetime.now(localtz)

# run if the time condition is satisfied
def timedRun(timeCheck, event):
    if timeCheck(getLocalTime()):
        event()
        return True
    return False

# run if the duration condition is satisfied
def durRun(durCheck, lastTime, event):
    if durCheck(getLocalTime(), lastTime):
        event()
        return True
    return False

# more than the specified period
# :param timedelta period
def mtsp(period): 
    return lambda now, past: now - past > period

# at a specific time of the day
# :param datetime time
def at_tod(time):
    return lambda now: (time.hour, time.minute) == (now.hour, now.minute)

# whether on the specified day
# :param datetime time
def at_day(time):
    nowtime = getLocalTime()
    return (nowtime.year, nowtime.month, nowtime.day) == (time.year, time.month, time.day)

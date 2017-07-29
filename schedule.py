from datetime import datetime
import pytz

# timezone of Beijing
BeijingTZ = pytz.timezone('Asia/Shanghai')

# get UTC+8(Beijing) time, in datetime.datetime
def getBJTime():
    return datetime.now(BeijingTZ)

# run if the time condition is satisfied
def timerun(timecheck, event):
    if timecheck(getBJTime()):
        event()

# run if the duration condition is satisfied
def durrun(durcheck, lasttime, event):
    if durcheck(getBJTime(), lasttime):
        event()




from datetime import datetime
import pytz

# timezone of Beijing
BeijingTZ = pytz.timezone('Asia/Shanghai')

# get UTC+8(Beijing) time, in datetime.datetime
def getBJTime():
    return datetime.now(BeijingTZ)

"""
    ltns.py: to see if a user is a "long-time-no-see" one
            or is his/her first show up in the chat
"""
import timeman

lastshow = {}

def lastshowuptime(userid):
    if userid not in lastshow:
        return timeman.getLocalTime()
    else:
        temp = lastshow[userid]
        return temp

def showup_update(userid):
    lastshow[userid] = timeman.getLocalTime()
    print("Update:", userid, lastshow[userid])

# decorator
# run func(message) if the speaker hasn't shown up for a day
def ltns(func):
    def gtr(message):
        
        timeman.durRun(timeman.mtsp(timeman.a_day), 
            lastshowuptime(message.from_user.id),
            lambda : func(message)
        )
        showup_update(message.from_user.id) 
    return gtr
    

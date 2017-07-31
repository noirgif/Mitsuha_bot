"""
    zaowan.py: zao in the morning and wan at night
"""
import daily
import genericMessage as gm
import os


class Zao:
    def __init__(self, bot, message):
        sendzao = lambda : gm.msg(("text", {"chat.id":message.chat.id,
"text":"/zao@zao_bot"})).send(bot)
        self.task = daily.dailyTask((5, 0), sendzao)

    def destroy(self):
        self.task.destroy()


class Wan:
    def __init__(self, bot, message):
        sendwan = lambda : gm.msg(("text", {"chat.id":message.chat.id,
"text":"/wan@wan_bot"})).send(bot)
        self.task = daily.dailyTask((23, 0), sendwan)

    def destroy(self):
        self.task.destroy()

def poll():
    # fork a process to check
    daily.daily_task_check()

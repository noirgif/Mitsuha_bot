import telebot
import json
import random
from muagay import *
import ltns
import zaowan as zw
import os
import time

# get token
TokenFile = open('config/token.json')
Token = json.load(TokenFile)["TOKEN"]
TokenFile.close()

bot = telebot.TeleBot(Token)

# gay reply
@bot.message_handler(regexp=r"(三爷.*给)|(给.*三爷)")
def gayer(message):
    send_gay(bot, message)

# reply to /start
@bot.message_handler(commands=['start'])
# reply to replies to me
@bot.message_handler(regexp=r"😘|(mua)|(可爱的)")
    #func=lambda msg: msg.reply_to_message and msg.reply_to_message.from_user.id == bot.get_me().id)
def mua_reply(message):
    send_mua(bot, message)

@bot.message_handler(func=lambda x: True)
@ltns.ltns
def ltns_greetings(message):
    send_mua(bot, message)    

tasklist = {}

@bot.message_handler(commands=['/startzaowan'])
def start_zaowan(message):
    if message.chat.id in tasklist:
        bot.reply_to(message, "Error 0x524523: Tasks already scheduled!")
    else:
        tasklist[message.chat.id] = (zw.Zao(bot, message), zw.Wan(bot, message))
        bot.reply_to(message, "Done!")
        zw.poll()

@bot.message_handler(commands=['/stopzaowan'])
def stop_zaowan(message):
    if message.chat.id not in tasklist:
        bot.reply_to(message, "Error 0x524524: No schedule now!")
    else:
        for task in tasklist[message.chat.id]:
            task.destroy()
        bot.reply_to(message, "Done!")


bot.polling(none_stop= True)

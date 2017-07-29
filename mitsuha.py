import telebot
import json
import random
from muagay import *
import ltns

# get token
TokenFile = open('config/token.json')
Token = json.load(TokenFile)["TOKEN"]
TokenFile.close()

bot = telebot.TeleBot(Token)
def send_welcome(message):
    # using the global bot variable
    send_mua(bot, message)

# gay reply
@bot.message_handler(regexp=r"(三爷.*给)|(给.*三爷)")
def gayer(message):
    send_gay(bot, message)

# reply to /start
@bot.message_handler(commands=['start'])
# reply to replies to me
@bot.message_handler(regexp=r"😘",
    func=lambda msg: msg.reply_to_message and msg.reply_to_message.from_user == bot.getMe())
def gay_reply(message):
    send_mua(bot, message)

@bot.message_handler(func=lambda x: True)
@ltns.ltns
def ltns_greetings(message):
    send_mua(bot, message)    

bot.polling()

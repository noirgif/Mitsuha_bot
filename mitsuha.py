import telebot
import json
import random
import getBJTime
import genericMessage
import secrets

# get token
TokenFile = open('config/token.json')
Token = json.load(TokenFile)["TOKEN"]
TokenFile.close()

bot = telebot.TeleBot(Token)

def gen_mua_messages(message):
    return list(map(genericMessage.msg,
            [("text",{"chat.id":message.chat.id,
                    "text":"mua"}),
            ("text",{"chat.id":message.chat.id,
                    "text":"😘"*random.randint(1, 7)})
            ("sticker", {"chat.id":message.chat.id,
                    "sticker":"CAADBQADKgIAAvjGxQqRuFhOXjA2SAI"})
            ]))
            
def gen_gay_messages(message):
    return list(map(genericMessage.msg,
            [("sticker",{"chat.id":message.chat.id,
                        "reply_to_message_id":message.message_id,
                        "sticker":"CAADBQADXgADNYDMDnvpH22TGWSTAg"})
            ]))

@bot.message_handler(commands=['start'])
def send_welcome(message):
    # using the global bot variable
    send_mua(bot, message)

@bot.message_handler(regexp=r"(三爷.*给)")
def gayer(message):
    print(message.chat.id, message.text)
    send_gay(bot, message)

#sendmua: reply with mua
def send_mua(bot, message):
    secrets.choice(gen_mua_messages(message)).send(bot)

#sendgay: reply to gay messages
def send_gay(bot, message):
    secrets.choice(gen_gay_messages(message)).send(bot)

bot.polling()

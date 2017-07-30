import genericMessage
import secrets
import json
import random

# nickname_list
nicklist = json.load(open('config/nickname.json'))
idlist = {}

def gen_mua_messages(message):
    return list(map(genericMessage.msg,
            [("text",{"chat.id":message.chat.id,
                      "reply_to_message_id": message.message_id,
                    "text":"mua"}),
            ("text",{"chat.id":message.chat.id,
                      "reply_to_message_id": message.message_id,
                    "text":"😘"*random.randint(1, 3)}),
            # todo: more than 3 kissing emojis if replied with it
            ("sticker", {"chat.id":message.chat.id,
                      "reply_to_message_id": message.message_id,
                    "sticker":"CAADBQADKgIAAvjGxQqRuFhOXjA2SAI"})
            ]))
            
def gen_gay_messages(message):
    return list(map(genericMessage.msg,
            [("sticker",{"chat.id":message.chat.id,
                    "reply_to_message_id":message.message_id,
                    "sticker":"CAADBQADXgADNYDMDnvpH22TGWSTAg"}),
             ("list", [("text", {"chat.id":message.chat.id,
                    "text":"不给"}),
                ("text", {"chat.id":message.chat.id,
                    "text":"我是女孩子"})
                       ])
            ]))

#sendmua: reply with mua
def send_mua(bot, message):
    secrets.choice(gen_mua_messages(message)).send(bot)

#sendgay: reply to gay messages
def send_gay(bot, message):
    secrets.choice(gen_gay_messages(message)).send(bot)

def get_nickname(message):
    # since the user id is unknown, the first name is used
    if nicklist.get(message.from_user.id):
        return nicklist[message.from_user.id]
    else:
        idlist[message.from_user.username] = message.from_user.id
        filex = open('data/idlist.json','wb')
        json.dump(idlist, filex)
        filex.close()
        print(message.from_user.id)
    # do not reply if the nickname is unknown
        return None

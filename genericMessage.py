class msg:
    # _type is a string indicating the type of the message
    # it could be either text, sticker, or photo
    # self.content is a dictionary containing the info of the message
    def __init__(self, pair):
        self._type = pair[0] 
        self.content = pair[1]
    
    def send(self, telebot):
        if (self._type == "text"):
            telebot.send_message(chat_id=self.content.get("chat.id"),
                                text=self.content.get("text"),
                                parse_mode=self.content.get("parse_mode"),
                                disable_web_page_preview=self.content.get("disable_web_page_preview"),
                                disable_notification=self.content.get("disable_notification"),
                                reply_to_message_id=self.content.get("reply_to_message_id"),
                                reply_markup=self.content.get("reply_markup"))
        if (self._type == "photo"):
            telebot.send_photo(chat_id=self.content.get("chat.id"),
                                photo=self.content.get("photo"),
                                caption=self.content.get("caption"),
                                disable_notification=self.content.get("disable_notification"),
                                reply_to_message_id=self.content.get("reply_to_message_id"),
                                reply_markup=self.content.get("reply_markup"))
        if (self._type == "sticker"):
            telebot.send_sticker(chat_id=self.content.get("chat.id"),
                                data=self.content.get("sticker"),
                                disable_notification=self.content.get("disable_notification"),
                                reply_to_message_id=self.content.get("reply_to_message_id"),
                                reply_markup=self.content.get("reply_markup"))
        # list: a list of messages
        if (self._type == "list"):
            for message in map(msg, self.content):
                message.send(telebot)
        # todo: other formats

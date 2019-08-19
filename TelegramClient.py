from pyrogram import Client, Filters
from pyrogram.api.functions.messages.edit_chat_admin import EditChatAdmin


api_id = "956114"
api_hash = "fb3e9d5d801a823983d487640bcb8f55"

lastChatID = None

class TelegramAPI():
    def __init__(self, client):
        self.app = client

    def send_message(self, id, message):
        return self.app.send_message(id, message)

    def create_chat(self, title, users):
        return self.app.create_group(title, users)

    def add_members(self, chat_id, users):
        return self.app.add_chat_members(chat_id, users)

    def kick_members(self, chat_id, user):
        return self.app.kick_chat_member(chat_id, user)

    def pin_message(self, chat_id, message_id, notify):
        return self.app.pin_chat_message(chat_id, message_id, notify)

    def unpin_message(self, chat_id):
        return self.app.unpin_chat_message(chat_id)

    def set_chat_title(self, chat_id, title):
        return self.app.set_chat_title(chat_id, title)

with Client('session', api_id, api_hash) as client:
    t = TelegramAPI(client)
    print(t.create_chat())

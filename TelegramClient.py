from pyrogram import Client, Filters, Chat
from pyrogram.api.functions.messages.edit_chat_admin import EditChatAdmin
from pyrogram.api.types import InputUser
from pyrogram.api.types import InputUserEmpty, InputUserSelf, InputUser
from pyrogram.api.functions.users import GetFullUser


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


if __name__ == "__main__":
    api_id = "956114"
    api_hash = "fb3e9d5d801a823983d487640bcb8f55"

    lastChatID = None
    with Client('anon', api_id, api_hash) as client:
        class A:
            def __init__(self, id):
                self.id = id

            def write(self):
                return bytes(self.id, encoding='utf-8')


        print(client.get_users('zakhar123'))
        # _ = InputUserSelf()
        # print(_)
        print(client.send(GetFullUser(id=InputUserSelf()))['user'])

        client.send(EditChatAdmin(
            chat_id=324493059,
            user_id=InputUser(user_id=413679270, access_hash=client.send(GetFullUser(id=InputUserSelf()))['user']["access_hash"]*-1),
            is_admin=True
        ))

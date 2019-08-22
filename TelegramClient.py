from pyrogram import Client

class TelegramAPI():
    def __init__(self, client):
        self.app = client

    def send_message(self, id, message):
        return self.app.send_message(id, message)

    def create_chat(self, title, description, users):
        chat = self.app.create_supergroup(title, description)
        TelegramAPI(self.app).add_admin(chat["id"], users)
        return chat

    def add_members(self, chat_id, users):
        return self.app.add_chat_members(chat_id, users)

    def kick_members(self, chat_id, user):
        return self.app.kick_chat_member(chat_id, user)

    def pin_message(self, chat_id, message_id):
        return self.app.pin_chat_message(chat_id, message_id, True)

    def unpin_message(self, chat_id):
        return self.app.unpin_chat_message(chat_id)

    def set_chat_title(self, chat_id, title):
        return self.app.set_chat_title(chat_id, title)

    def add_admin(self, chat_id, users):
        self.app.add_chat_members(chat_id, users)
        if isinstance(users, str) is True:
            users = [users]
        for i in users:
            self.app.promote_chat_member(chat_id, i, can_pin_messages=True, can_promote_members=True)
        return True

if __name__ == "__main__":
    api_id = "token"
    api_hash = "token"

    with Client('session', api_id, api_hash) as client:
        t = TelegramAPI(client)
        print(t.function(arguments))

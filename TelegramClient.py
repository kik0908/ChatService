class TelegramAPI:
    def __init__(self, client):
        self.app = client

    def chat_permission(self, chat_id):
        class ChatPermission:
            def __init__(
                    self,
                    send_message: bool = True,
                    send_media_messages: bool = True,
                    send_other_messages: bool = True,
                    add_web_page_previews: bool = True,
                    send_polls: bool = True,
                    change_info: bool = False,
                    invite_users: bool = False,
                    pin_messages: bool = False
            ):
                self.can_send_messages = send_message
                self.can_send_media_messages = send_media_messages
                self.can_send_other_messages = send_other_messages
                self.can_add_web_page_previews = add_web_page_previews
                self.can_send_polls = send_polls
                self.can_change_info = change_info
                self.can_invite_users = invite_users
                self.can_pin_messages = pin_messages

        return self.app.set_chat_permissions(chat_id, ChatPermission())

    def set_member(self, chat_id, users):
        class MemberPermission:
            def __init__(
                    self,
                    change_info: bool = False,
                    invite_users: bool = False,
                    pin_messages: bool = False,
                    send_message: bool = True,
                    send_media_messages: bool = True,
                    send_other_messages: bool = True,
                    add_web_page_previews: bool = True,
                    send_polls: bool = True
            ):
                self.can_send_messages = send_message
                self.can_send_media_messages = send_media_messages
                self.can_send_other_messages = send_other_messages
                self.can_add_web_page_previews = add_web_page_previews
                self.can_send_polls = send_polls
                self.can_change_info = change_info
                self.can_invite_users = invite_users
                self.can_pin_messages = pin_messages

        if isinstance(users, str) is True:
            users = [users]
        for i in users:
            self.app.restrict_chat_member(chat_id, i, MemberPermission())
        return True

    def set_admin(self, chat_id, users):
        class AdminPermission:
            def __init__(
                    self,
                    change_info: bool = True,
                    invite_users: bool = True,
                    pin_messages: bool = True,
                    send_message: bool = True,
                    send_media_messages: bool = True,
                    send_other_messages: bool = True,
                    add_web_page_previews: bool = True,
                    send_polls: bool = True
            ):
                self.can_send_messages = send_message
                self.can_send_media_messages = send_media_messages
                self.can_send_other_messages = send_other_messages
                self.can_add_web_page_previews = add_web_page_previews
                self.can_send_polls = send_polls
                self.can_change_info = change_info
                self.can_invite_users = invite_users
                self.can_pin_messages = pin_messages

        if isinstance(users, str) is True:
            users = [users]
        for i in users:
            self.app.restrict_chat_member(chat_id, i, AdminPermission())
        return True

    def send_message(self, id, message):
        return self.app.send_message(id, message)

    def create_chat(self, title, users):
        chat_info = self.app.create_group(title, users)
        self.set_admin(chat_info['id'], users)
        return chat_info

    def add_members(self, chat_id, users):
        self.app.add_chat_members(chat_id, users)
        TelegramAPI(self.app).set_member(chat_id, users)
        return True

    def kick_members(self, chat_id, user):
        return self.app.kick_chat_member(chat_id, user)

    def pin_message(self, chat_id, message_id, notify):
        return self.app.pin_chat_message(chat_id, message_id, notify)

    def unpin_message(self, chat_id):
        return self.app.unpin_chat_message(chat_id)

    def set_chat_title(self, chat_id, title):
        return self.app.set_chat_title(chat_id, title)

    def add_admin(self, chat_id, user_id):
        return self.app.add_chat_members(chat_id, user_id)


if __name__ == "__main__":
    from pyrogram import Client

    api_id = "token"
    api_hash = "token"

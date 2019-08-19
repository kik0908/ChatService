import pyrogram
from pyrogram.client.methods.chats.create_group import CreateGroup
from pyrogram.api.functions.messages import EditChatAdmin


from utils import get_config

print(get_config())
with pyrogram.Client('anon', get_config()['api_id'], get_config()['api_hash']) as client:
    _ = client.get_users(['dr3al'])
    client.send(EditChatAdmin(chat_id=-3, user_id=12, is_admin=True), 5, 100)
    print(type(_), _)
    client.create_group("", 'dr3al')

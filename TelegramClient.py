import pyrogram
from pyrogram.client.methods.chats.create_group import CreateGroup

from utils import get_config

print(get_config())
with pyrogram.Client('anon', get_config()['api_id'], get_config()['api_hash']) as client:
    _ = client.get_users(['dr3al'])
    print(type(_), _)
    client.create_group("", 'dr3al')

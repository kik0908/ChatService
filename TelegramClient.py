from telethon import TelegramClient

api_id = xxxxxx
api_hash = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'

with TelegramClient('anon', api_id, api_hash) as client:
    while True:
        client.loop.run_until_complete(client.send_message('username', 'text_message'))

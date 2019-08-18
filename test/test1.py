import telethon.tl.functions.channels as awe
import telethon


async def get_dialogs():
    _ = []
    async for dialog in client.iter_dialogs():
        _.append((dialog.name, dialog.id))
    return _


def search_for_name(array, name):
    for i in array:
        if i[0] == name:
            return i


async def aaa():
    print(dir(awe.CreateChannelRequest("dfdfd", "123")))


a = awe.CreateChannelRequest
b = awe.JoinChannelRequest

with telethon.TelegramClient('kirya', 909539, "a12eb4721c43134281322f396a4d8750") as client:
    chat_name = "123"
    client(awe.CreateChannelRequest("dfdfd", "123"))
    id = search_for_name(client.loop.run_until_complete(get_dialogs()), chat_name)
    print(client.loop.run_until_complete(get_dialogs()))

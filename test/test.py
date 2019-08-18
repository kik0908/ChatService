import telethon


async def get_dialogs():
    _ = []
    async for dialog in client.iter_dialogs():
        _.append((dialog.name, 'has ID', dialog.id))
    return _


def a():
    for message in client.iter_messages(-336651450):
        if message.buttons is not None:
            but = message.buttons[0][0]
            return message.text, but


print('start')

with telethon.TelegramClient('kirya', 909539, "a12eb4721c43134281322f396a4d8750") as client:
    print('connect')
    ff = a()
    while True:
        aa = ff[0].split('\n')[2].split()[2]
        if aa != 'Kirya':
            client.loop.run_until_complete(ff[1].click())
            print(f'I`m click! U not first. {aa} first')
        else:
            print('I`M FIRST')

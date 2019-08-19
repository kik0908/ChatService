from json import load, dump


def get_config() -> dict:
    """
    Возвращает словарь с параметрами из конфига

    :return:
    """
    with open('config.json') as file:
        ans: dict = load(file)

    if ans["use_local_config"] is True:
        try:
            with open('local_config.json') as file:
                _data = load(file)
                for key, val in _data.items():
                    ans[key] = val
        except FileNotFoundError:
            pass

    return ans


def add_chat_in_db(data: dict):
    try:
        with open('chats.json') as file:
            ans = load(file)
        ans['chats'].append(data)
    except:
        ans = {'chats': [data]}

    with open('chats.json', 'w') as file:
        dump(ans, file)

    return True


def get_chats_from_db() -> list:  # Если оставим, адаптировать к бин поиску
    try:
        with open('chats.json') as file:
            ans = load(file)
    except:
        ans = {'chats': []}

    return ans['chats']


def get_chat_from_id(id: int) -> dict:  # Если оставим, заюзать бин поиск
    chats = get_chats_from_db()
    for i in chats:
        if i['id'] == id:
            return i


def get_chat_from_name(name: str):  # Если оставим, заюзать бин поиск
    chats = get_chats_from_db()
    for i in chats:
        if i['title'] == name:
            return i


add_chat_in_db({'df': 123, 'fd': [1, 23, 4]})

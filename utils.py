from json import load


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
        except FileNotFoundError:
            pass

        for key, val in _data.items():
            ans[key] = val

    return ans


print(get_config())

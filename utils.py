from json import load, dump
import logging


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


def error_handler_for_http_answer(func):
    """
    Декоратор обработки ошибок для функций ответа на запросы
    Если в процессе выполнения потенциально опасного кода вызвался Exception, будет возвращено описание ошибки и код 502
    :param func:
    :return:
    """

    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as E:
            logging.error(str(E))
            return str(E), 502

    return wrapper


def banchmark():
    pass
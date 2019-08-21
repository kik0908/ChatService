from json import load, dump
import logging
from time import time


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
            print("Error:", E)
            return str(E), 502

    return wrapper


def banchmark(iters=1, active=True):
    def wrapper(func):
        def wrapper2(*args, **kwargs):
            if active is True:
                total = 0
                for i in range(iters):
                    start = time()
                    ans = func(*args, **kwargs)
                    end = time()
                    total += end - start
                print('Среднее время выполнения функции:', total / iters)

            return func(*args, **kwargs)

        return wrapper2

    return wrapper

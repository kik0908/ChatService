import logging

import server
from utils import get_config

levels = {'warning': logging.WARNING, 'info': logging.INFO, 'debug': logging.DEBUG, 'error': logging.ERROR}
if __name__ == "__main__":
    _config = get_config()

    logging.basicConfig(filename=_config["log_file_name"], level=levels[_config['log_level']])

    server.start(_config["port"], _config["port"])

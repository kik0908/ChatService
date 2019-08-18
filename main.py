import logging

import server
from utils import get_config

if __name__ == "__main__":
    _config = get_config()

    logging.basicConfig(filename=_config["log_file_name"], level=logging.INFO)

    server.start(_config["host"], _config["port"], _config["port"])

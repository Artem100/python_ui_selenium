import json
import logging
import os
from pathlib import Path


def read_json_file(file_path):
    logging.info("Read data from file: '{}'".format(file_path))
    # with open(file_path) as f:
    with open((os.path.join(file_path)), "r") as f:
        data = json.loads(f.read())
    return data
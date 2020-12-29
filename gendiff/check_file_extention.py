import json
import yaml
import os
from json.decoder import JSONDecodeError
from yaml.scanner import ScannerError


def check_extension(file_name):
    root_ext = os.path.splitext(file_name)
    if root_ext[1] == '.json':
        try:
            with open(file_name, 'r') as file:
                return json.load(file)
        except JSONDecodeError:
            raise RuntimeError("This is not valid JSON file")
    elif root_ext[1] == '.yml':
        try:
            with open(file_name, 'r') as file:
                return yaml.load(file, Loader=yaml.FullLoader)
        except ScannerError:
            raise RuntimeError("This is not valid Yaml file")
    else:
        raise RuntimeError("This file extention is incorrect")

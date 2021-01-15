import json
import yaml
import os


def getting_file_data(file_path):
    _, ext = os.path.splitext(file_path)
    try:
        with open(file_path, 'r') as file:
            if ext.lower() == '.json':
                return json.load(file)
            elif ext.lower() == '.yml' or ext.lower() == '.yaml':
                return yaml.load(file, Loader=yaml.FullLoader)
    except :
        raise RuntimeError("File extention is incorrect")

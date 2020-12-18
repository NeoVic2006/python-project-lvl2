import json


def json_formatter(file):
    return json.dumps({'data': file}, indent=2)

from gendiff.formatters.stylish import stylish_formatter
from gendiff.formatters.plain import plain_formatter
from gendiff.formatters.json import json_formatter


DEFAULT_STYLE = "stylish"
JSON_STYLE = "json"
PLAIN_STYLE = "plain"


def cheking_format(data, format):
    if format == JSON_STYLE:
        return json_formatter(data)
    elif format == PLAIN_STYLE:
        return plain_formatter(data)
    elif format == DEFAULT_STYLE:
        return stylish_formatter(data)
    else:
        raise RuntimeError("This is not valid Format")

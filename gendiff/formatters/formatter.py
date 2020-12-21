from gendiff.formatters.stylish import stylish_formatter
from gendiff.formatters.plain import plain_formatter
from gendiff.formatters.json import json_formatter


def formatters(data, format):
    if format == "json":
        return json_formatter(data)
    elif format == "plain":
        return plain_formatter(data)
    format == "stylish"
    return stylish_formatter(data)

from gendiff.formatters.stylish import stylish_formatter
from gendiff.formatters.plain import plain_formatter
from gendiff.formatters.json import json_formatter


DEFAULT_STYLE = "stylish"


def formatters(data, format):
    if format == "json":
        return json_formatter(data)
    elif format == "plain":
        return plain_formatter(data)
    elif format == DEFAULT_STYLE:
        return stylish_formatter(data)
    else:
        raise RuntimeError("This is not valid Format")

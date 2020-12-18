from gendiff.formatters.stylish import stylish
from gendiff.formatters.plain import plain


def formatter(data, format):
    if format == "stylish":
        return stylish(data)
    elif format == "plain":
        return plain(data)
    elif format == "json":
        return stylish(data)
    else:
        print("Wrong format option!")

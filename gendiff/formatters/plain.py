UNCHANGED = "same"
CHANGED = "old"
ADDED = "new"
UPDATED_OLD = "changed_old"
UPDATED_NEW = "changed_new"


def plain_formatter(file, path=''):
    strings = []
    chan_status = {}
    for i in file:
        if isinstance(i["value"], list):
            if i["status"] == UNCHANGED:
                strings.append("{}".format(
                    plain_formatter(i["value"],
                                    path=path + (i["name"] + "."))))
        if i["status"] == ADDED:
            strings.append("Property '{}{}' was added with value: {}"
                           .format(path, i["name"],
                                   _format_value(i["value"])))
        elif i["status"] == CHANGED:
            strings.append("Property '{}{}' was removed".format(
                path, i["name"]))
        elif i["status"] == UPDATED_OLD:
            chan_status = {"name": i["name"],
                           "value": i["value"]}
        elif i["status"] == UPDATED_NEW:
            strings.append("Property '{}{}' was updated. From {} to {}"
                           .format(path, i["name"],
                                   _format_value(chan_status["value"]),
                                   _format_value(i["value"])))
    return '\n'.join(strings)


def _format_value(value):
    string = ''
    if isinstance(value, list):
        string = '[complex value]'
    elif value is None:
        string = "null"
    elif value is True:
        string = "true"
    elif value is False:
        string = "false"
    elif type(value) == int or type(value) == float:
        string = value
    else:
        string = "'{}'".format(str(value))
    return string

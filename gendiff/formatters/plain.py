UNCHANGED = "same"
REMOVED = "old"
ADDED = "new"
UPDATED_OLD = "changed_old"
UPDATED_NEW = "changed_new"


def plain_formatter(file_data, path=''):
    lines = []
    chan_status = {}
    for line in file_data:
        if isinstance(line["value"], list):
            if line["status"] == UNCHANGED:
                lines.append("{}".format(
                    plain_formatter(line["value"],
                                    path=path + (line["name"] + "."))))
        if line["status"] == ADDED:
            lines.append("Property '{}{}' was added with value: {}"
                           .format(path, line["name"],
                                   _format_value(line["value"])))
        elif line["status"] == REMOVED:
            lines.append("Property '{}{}' was removed".format(
                path, line["name"]))
        elif line["status"] == UPDATED_OLD:
            chan_status = {"name": line["name"],
                           "value": line["value"]}
        elif line["status"] == UPDATED_NEW:
            lines.append("Property '{}{}' was updated. From {} to {}"
                           .format(path, line["name"],
                                   _format_value(chan_status["value"]),
                                   _format_value(line["value"])))
    return '\n'.join(lines)


def _format_value(value):
    if isinstance(value, dict) or isinstance(value, list):
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

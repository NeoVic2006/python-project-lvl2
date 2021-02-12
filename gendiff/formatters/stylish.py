STATUSES = {
    'new': "+",
    'old': "-",
    'same': " ",
    'changed': "-"
}


def stylish_formatter(file_data, spaces=0):
    string = '{'
    for i in file_data:
        string += "\n {} {} {}: ".format(spaces * " ",
                                         STATUSES[i['status']], i["name"])
        if i["status"] == 'changed':
            if isinstance(i["value"], list):
                string += stylish_formatter(i["value"], spaces + 4)
            else:
                string += _format_value(i["value"])
            string += "\n {} + {}: {}".format(spaces * " ",
                                              i["name"],
                                              _format_value(i["value_new"]))
        elif isinstance(i["value"], list):
            string += stylish_formatter(i["value"], spaces + 4)
        else:
            string += _format_value(i["value"])
    string += "\n{}}}".format((spaces) * " ")
    return string


def _format_value(value):
    if value is None:
        string = "null"
    elif value is True:
        string = "true"
    elif value is False:
        string = "false"
    else:
        string = str(value)
    return string

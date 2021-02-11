STATUSES = {
    'new': "+",
    'old': "-",
    'same': " ",
    'changed': " ",
    'dict': " "
}


def stylish_formatter(file_data, spaces=0):
    string = '{'
    for i in file_data:
        string += "\n {} {} {}: ".format(spaces * " ",
                                         STATUSES[i['status']], i["name"])
        if isinstance(i["value"], list) and isinstance(i["value"][0], dict):
            string += stylish_formatter(i["value"], spaces + 4)
        elif isinstance(i["value"], dict):
            string += _formating_dict_data(i["value"], spaces + 8)
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


def _formating_dict_data(value, spaces):
    string = '{'
    for i in value:
        string += "\n{}{}: ".format((spaces * " "), i)
        if isinstance(value[i], dict):
            string += _formating_dict_data(value[i], spaces + 4)
        else:
            string += _format_value(value[i])
    string += "\n{}}}".format((spaces - 4) * " ")
    return string

STATUSES = {
    'new': "+",
    'old': "-",
    'same': " ",
    'changed_old': "-",
    'changed_new': "+"
}


def stylish_formatter(file, spaces=2):
    string = '{'
    for i in file:
        string += "\n" + spaces * " " + STATUSES[i['status']]
        string += " " + i["name"] + ": "
        if isinstance(i["value"], list):
            string += stylish_formatter(i["value"], spaces + 4)
        else:

            string += _format_value(i["value"])
    string += "\n" + ((spaces - 2) * " ") + "}"
    return string


def _format_value(value):
    string = ''
    if value is None:
        string += "null"
    elif value is True:
        string += "true"
    elif value is False:
        string += "false"
    else:
        string += str(value)
    return string

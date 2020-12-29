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
        try:
            string += "\n" + spaces * " " + STATUSES[i['status']]
            string += " " + i["name"] + ": "
            if isinstance(i["value"], list) and isinstance(i["value"][0], dict):
                string += stylish_formatter(i["value"], spaces + 4)
            elif isinstance(i["value"], dict):
                string += _building_dict_tree(i["value"], spaces + 6)
            else:
                string += _format_value(i["value"])
        except:
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


def _building_dict_tree(value, spaces):
    string = '{'
    for i in value:
        string += "\n" + spaces * " " + i + ": "
        if isinstance(value[i], dict):
            string += _building_dict_tree(value[i], spaces + 4)
        else:
            string += _format_value(value[i])
    string += "\n" + ((spaces - 4) * " ") + "}"
    return string

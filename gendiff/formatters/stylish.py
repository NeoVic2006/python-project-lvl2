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
                string += _format_v(i["value"])

            if isinstance(i["value_new"], list):
                string += "\n {} + {}: {}".format(spaces * " ",
                                                  i["name"],
                                                  _format_v(stylish_formatter(
                                                            i["value_new"],
                                                            spaces + 4)))
            else:
                string += "\n {} + {}: {}".format(spaces * " ",
                                                  i["name"],
                                                  _format_v(i["value_new"]))
        elif isinstance(i["value"], list):
            string += stylish_formatter(i["value"], spaces + 4)
        else:
            string += _format_v(i["value"])
    string += "\n{}}}".format((spaces) * " ")
    return string


def _format_v(value):
    if value is None:
        string = "null"
    elif value is True:
        string = "true"
    elif value is False:
        string = "false"
    else:
        string = str(value)
    return string

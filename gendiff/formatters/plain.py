def plain_formatter(file, path=''):
    strings = []
    changed_status = {}
    for i in file:
        if isinstance(i["value"], list):
            if i["status"] == "same":
                strings.append("{}".format(
                    plain_formatter(i["value"],
                                    path=path + (i["name"] + "."))))
        if i["status"] == "new":
            strings.append("Property '{}{}' was added with value: {}".format(
                path, i["name"], _format_value(i["value"])))
        elif i["status"] == "old":
            strings.append("Property '{}{}' was removed".format(
                path, i["name"]))
        elif i["status"] == "changed_old":
            changed_status = {"name": i["name"],
                              "value": i["value"]}
        elif i["status"] == "changed_new":
            strings.append("Property '{}{}' was updated. From {} to {}".format(
                path, i["name"], _format_value(changed_status["value"]
                                               ), _format_value(i["value"])))
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
    elif type(value) == int:
        string = value
    else:
        string = ("'" + str(value) + "'")
    return string

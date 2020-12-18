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
        if i["status"] == "old":
            strings.append("Property '{}{}' was removed".format(
                path, i["name"]))
        if i["status"] == "changed_old":
            changed_status = {"name": i["name"],
                              "value": i["value"]}
        if i["status"] == "changed_new":
            strings.append("Property '{}{}' was updated. From {} to {}".format(
                path, i["name"], _format_value(changed_status["value"]
                                               ), _format_value(i["value"])))
    return '\n'.join(strings)


def _format_value(value):
    if isinstance(value, list):
        return '[complex value]'
    else:
        if value is None:
            return "null"
        if value is True:
            return "true"
        if value is False:
            return "false"
        return ("'" + str(value) + "'")

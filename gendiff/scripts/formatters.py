from operator import itemgetter


status = {
    'new': "+",
    'old': "-",
    'same': " ",
    'changed_old': "-",
    'changed_new': "+"
}


def _stylish(file, spaces=2):
    file = sorted(file, key=itemgetter('name'))
    string = ' {'
    for i in file:
        string += "\n" + spaces*" " + status[i['status']] + " " + i["name"]
        if isinstance(i["value"], list):
            string += _stylish(i["value"], spaces + 4)
        else:
            if i["value"] is None:
                string += ": " + "null"
            if i["value"] is True:
                string += ": " + "true"
            else:
                string += ": " + str(i["value"])
    string += "\n" + ((spaces-2)*" ") + "}"
    return string


def _plain(file, path=''):
    file = sorted(file, key=itemgetter('name'))
    strings = []
    changed_status = {}
    for i in file:
        if isinstance(i["value"], list):
            if i["status"] == "same":
                strings.append("{}".format(
                    _plain(i["value"], path=path + (i["name"] + "."))))
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


def formatter(data, format):
    if format == "stylish":
        return _stylish(data)
    elif format == "plain":
        return _plain(data)
    elif format == "json":
        return _stylish(data)
    else:
        print("Wrong format option!")

STATUSES = {
    'new': "+",
    'old': "-",
    'same': " ",
    'changed_old': "-",
    'changed_new': "+"
}


def stylish_formatter(file, spaces=2):
    string = ' {'
    for i in file:
        string += "\n" + spaces*" " + STATUSES[i['status']] + " " + i["name"]
        if isinstance(i["value"], list):
            string += stylish_formatter(i["value"], spaces + 4)
        else:
            if i["value"] is None:
                string += ": " + "null"
            if i["value"] is True:
                string += ": " + "true"
            else:
                string += ": " + str(i["value"])
    string += "\n" + ((spaces-2)*" ") + "}"
    return string

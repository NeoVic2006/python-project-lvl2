status = {
    'new': "+",
    'old': "-",
    'same': " "
}

def stylish(file, spaces=2):
    string = ' {'
    for i in file:
        string += "\n" + spaces*" " + status[i['status']] + " " + str(i["name"])
        if isinstance(i["value"], list):
            string += stylish(i["value"], spaces + 4)
        else:
            string += ": " + str(i["value"])

    string += "\n" + spaces*" " + "}"
    return string

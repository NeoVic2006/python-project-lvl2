status = {
    'new': "+",
    'old': "-",
    'same': " "
}

def stylish(file, spaces=2):
    string = ' {'
    for i in file:
        if isinstance(i["value"], dict):
            string += "\n" + spaces*" " + status[i['status']] + " " + str(i["name"]) + unpaking_dict(i["value"], spaces + 4)
        else: 
            string += "\n" + spaces*" " + status[i['status']] + " " + str(i["name"])
            if isinstance(i["value"], list):
                string += stylish(i["value"], spaces + 4)
            else:
                string += ": " + str(i["value"])

    string += "\n" + spaces*" " + "}"
    return string


def unpaking_dict(dictionary, spaces):
    string = ' {'
    for i in dictionary:
        if isinstance(dictionary[i], dict):
            string += "\n" + spaces*" "+ " " + str(i)
            string += unpaking_dict(dictionary[i], spaces + 4)
        else:
            string += "\n" + spaces*" " + str(" " + i + ": " + str(dictionary[i]))
    string += "\n" + spaces*" " + "}"
    return string

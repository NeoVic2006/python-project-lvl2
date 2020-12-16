status = {
    'new': "+",
    'old': "-",
    'same': " "
}


def stylish(file, spaces=2):
    string = ' {'
    for i in file:
        string += "\n" + spaces*" " + status[i['status']] + " " + i["name"]
        if isinstance(i["value"], list):
            string += stylish(i["value"], spaces + 4)
        else:
            if i["value"] is None:
                string += ": " + "null"
            else:
                string += ": " + str(i["value"])
    string += "\n" + ((spaces-2)*" ") + "}"
    return string


def formatter(data, format):
    if format == "stylish":
        return stylish(data)
    elif format == "flat":
        return stylish(data)
    elif format == "json":
        return stylish(data)
    else:
        print("Wrong format option!")

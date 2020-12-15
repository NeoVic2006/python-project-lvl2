from operator import itemgetter


status = {
    'new': "+",
    'old': "-",
    'same': " "
}


def stylish(file, spaces=2):
    file = sorted(file, key=itemgetter('name'))
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

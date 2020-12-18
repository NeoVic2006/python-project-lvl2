from operator import itemgetter


status = {
    'new': "+",
    'old': "-",
    'same': " ",
    'changed_old': "-",
    'changed_new': "+"
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
            if i["value"] is True:
                string += ": " + "true"
            else:
                string += ": " + str(i["value"])
    string += "\n" + ((spaces-2)*" ") + "}"
    return string

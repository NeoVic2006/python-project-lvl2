
status = {
    'new': "+",
    'old': "-",
    'same': " "
}



def stylish(file):

    string = '{'
    for i in file:
        string += "\n" + status[i['status']] + " " + str(i["name"])
        if isinstance(i["value"], list):
            string += stylish(i["value"])
        else:
            string += ": " + str(i["value"])
    string += "\n}"
    return string











def stylish123(file):

    string = '{'
    for i in file:
        if isinstance(i["value"], list):
            string += " \n" + "  " + str(status[i['status']]) + str(i["name"]) + " " + stylish(i["value"])
        else:
            string += " \n" + "      " + str(status[i['status']]) + " " + str(i["name"]) + ": " + str(i["value"])
    string += " \n }"
    return string

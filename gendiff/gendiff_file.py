import json


def generate_diff_JSON(json_file_1, json_file_2):
    json1 = reading_json_file(json_file_1)
    json2 = reading_json_file(json_file_2)

    result = ('{ ' + '\n')
    unique_keys_file2 = json2.keys() - json1.keys()

    if len(unique_keys_file2) != 0:
        for key in unique_keys_file2:
            result = result + ("  + "+str(key)+": " + str(json2[key]))

    for key, value in json1.items():
        if key in json2:
            if value == json2[key]:
                result = result + ('\n' + "    " +
                                   str(key) + ": " + str(json2[key]))
            else:
                result = result + ('\n' + "  - " +
                                   str(key) + ": " + str(value))
                result = result + ('\n' + "  + " +
                                   str(key) + ": " + str(json2[key]))
        else:
            result = result + ('\n' + "  - " + str(key) + ": " + str(value))
    result = result + ('\n' + '}')
    return result


def generate_diff_YAML(yml_file_1, yml_file_2):
    print("YAML start")


def reading_json_file(filename):
    with open(filename) as json_file:
        return json.load(json_file)

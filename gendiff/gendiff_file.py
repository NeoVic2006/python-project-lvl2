import json
import yaml


def generate_diff_JSON(json_file_1, json_file_2):
    json1 = reading_json_file(json_file_1)
    json2 = reading_json_file(json_file_2)
    print(json1, json2)
    return comparing_files(json1, json2)


def generate_diff_YAML(yml_file_1, yml_file_2):
    yaml1 = yaml.load(open(yml_file_1, 'r'), Loader=yaml.FullLoader)
    yaml2 = yaml.load(open(yml_file_2, 'r'), Loader=yaml.FullLoader)
    print(yaml1, yaml2)
    return comparing_files(yaml1, yaml2)


def reading_json_file(filename):
    with open(filename) as json_file:
        return json.load(json_file)


def comparing_files(file1, file2):
    result = ('{ ' + '\n')
    unique_keys_file2 = file2.keys() - file1.keys()

    if len(unique_keys_file2) != 0:
        for key in unique_keys_file2:
            result = result + ("  + "+str(key)+": " + str(file2[key]))

    for key, value in file1.items():
        if key in file2:
            if value == file2[key]:
                result = result + ('\n' + "    " +
                                   str(key) + ": " + str(file2[key]))
            else:
                result = result + ('\n' + "  - " +
                                   str(key) + ": " + str(value))
                result = result + ('\n' + "  + " +
                                   str(key) + ": " + str(file2[key]))
        else:
            result = result + ('\n' + "  - " + str(key) + ": " + str(value))
    result = result + ('\n' + '}')
    return result

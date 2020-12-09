import json
import os


def generate_diff(json_file_1, json_file_2):

    '''
    json_file_1 = json.load(open('C:\\Python_Work_for_Hexlet\\python-project-lvl2\\tests\\fixtures\\files\\file1.json'))
    json_file_2 = json.load(open('C:\\Python_Work_for_Hexlet\\python-project-lvl2\\tests\\fixtures\\files\\file2.json'))
    
    json_file_1 = json.load(open('/mnt/c/Python_Work_for_Hexlet/python-project-lvl2/tests/fixtures/files/file1.json'))
    json_file_2 = json.load(open('/mnt/c/Python_Work_for_Hexlet/python-project-lvl2/tests/fixtures/files/file2.json'))
    '''
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



def reading_json_file(filename):
    path = os.getcwd()
    print(path)
    with open(filename) as json_file:
        return json.load(json_file)
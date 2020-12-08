import json


def generate_diff(file_name1, file_name2):
    
    json_file_1 = json.load(open('C:\\Python_Work_for_Hexlet\\python-project-lvl2\\tests\\fixtures\\files\\file1.json'))
    json_file_2 = json.load(open('C:\\Python_Work_for_Hexlet\\python-project-lvl2\\tests\\fixtures\\files\\file2.json'))
    '''
    json_file_1 = json.load(open('/mnt/c/Python_Work_for_Hexlet/python-project-lvl2/tests/fixtures/files/file1.json'))
    json_file_2 = json.load(open('/mnt/c/Python_Work_for_Hexlet/python-project-lvl2/tests/fixtures/files/file2.json'))
    '''
    result = ('{ ' + '\n')

    unique_keys_file2 = json_file_2.keys() - json_file_1.keys()

    if len(unique_keys_file2) != 0:
        for key in unique_keys_file2:
            result = result + ("  + "+str(key)+": " + str(json_file_2[key]))
    for key, value in json_file_1.items():
        if key in json_file_2:
            if value == json_file_2[key]:
                result = result + ('\n' + "    " +
                                   str(key) + ": " + str(json_file_2[key]))
            else:
                result = result + ('\n' + "  - " +
                                   str(key) + ": " + str(value))
                result = result + ('\n' + "  + " +
                                   str(key) + ": " + str(json_file_2[key]))
        else:
            result = result + ('\n' + "  - " + str(key) + ": " + str(value))
    result = result + ('\n' + '}')
    return result

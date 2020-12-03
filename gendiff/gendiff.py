import json
import os


def generate_diff():
    my_absolute_dirpath = os.path.abspath(os.path.dirname(__file__))
    print(my_absolute_dirpath)
    file_p1 = json.load(open('/mnt/c/Python_Work_for_Hexlet/files/file1.json'))
    file_p2 = json.load(open('/mnt/c/Python_Work_for_Hexlet/files/file2.json'))

    result = ('{ ' + '\n')
    unique_keys_file2 = file_p2.keys() - file_p1.keys()
    if len(unique_keys_file2) != 0:
        for key in unique_keys_file2:
            result = result + ("  + " + str(key) + ": " + str(file_p2[key]))
    for key, value in file_p1.items():
        if key in file_p2:
            if value == file_p2[key]:
                result = result + ('\n' + "    " +
                                   str(key) + ": " + str(file_p2[key]))
            else:
                result = result + ('\n' + "  - " +
                                   str(key) + ": " + str(value))
                result = result + ('\n' + "  + " +
                                   str(key) + ": " + str(file_p2[key]))
        else:
            result = result + ('\n' + "  - " + str(key) + ": " + str(value))
    result = result + ('\n' + '}')
    return result

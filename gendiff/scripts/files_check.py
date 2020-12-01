import json



file_path1 = json.load(open('C:\Python_Work_for_Hexlet\python-project-lvl2\\files\\file1.json'))
file_path2 = json.load(open('C:\Python_Work_for_Hexlet\python-project-lvl2\\files\\file2.json'))


def generate_diff(file_path1, file_path2):
    result = ('{ ' + '\n') 
    unique_keys_file2 = file_path2.keys() - file_path1.keys()

    if len(unique_keys_file2) != 0:
        for key in unique_keys_file2:
            result = result + ("  + " + str(key) + ": " + str(file_path2[key]))

    for key, value in file_path1.items():
        if key in file_path2:
            if value == file_path2[key]:
                result = result + ('\n' + "    " + str(key) + ": " + str(file_path2[key]))
            else:
                result = result + ('\n' + "  - " + str(key) + ": " + str(value))
                result = result + ('\n' + "  + " + str(key) + ": " + str(file_path2[key]))
        else:
            result = result + ('\n' + "  - " + str(key) + ": " + str(value))       
    result = result + ('\n' + ' }')

    return result 

print(generate_diff(file_path1, file_path2))




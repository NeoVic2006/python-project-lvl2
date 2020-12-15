import json
import yaml


def generate_diff_JSON(json_file_1, json_file_2):
    json1 = json.load(open(json_file_1))
    json2 = json.load(open(json_file_2))
    return comparing_files(json1, json2)


def generate_diff_YAML(yml_file_1, yml_file_2):
    yaml1 = yaml.load(open(yml_file_1, 'r'), Loader=yaml.FullLoader)
    yaml2 = yaml.load(open(yml_file_2, 'r'), Loader=yaml.FullLoader)
    return comparing_files(yaml1, yaml2)


def comparing_files(file1, file2):
    new_keys = file2.keys() - file1.keys()
    old_keys = file1.keys() - file2.keys()
    same_keys = file1.keys() - new_keys - old_keys

    result = []

    for i in same_keys:
        if isinstance(file1[i], dict) and isinstance(file2[i], dict):
            result.append({"name": i,
                           "value": comparing_files(file1[i], file2[i]),
                           "status": "same"})
        else:
            if file1[i] == file2[i]:
                result.append(_single_file_check(i, file2, "same"))
            else:
                result.append(_single_file_check(i, file1, "old"))
                result.append(_single_file_check(i, file2, "new"))

    for i in old_keys:
        result.append(_single_file_check(i, file1, "old"))
    
    for i in new_keys:
        result.append(_single_file_check(i, file2, "new"))
    
    return result

'''
def _keys_check(keys, file):
    result = []
    for i in keys:
        result.append(_single_file_check(i, file, "new"))
    return result
'''

def _single_file_check(i, file, status):
    if isinstance(file[i], dict):
        return {"name": i,
                "value": comparing_files(file[i], file[i]),
                "status": status}
    else:
        return {"name": i, "value": file[i], "status": status}




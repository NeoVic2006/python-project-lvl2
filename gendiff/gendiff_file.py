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
                result.append({"name": i, "value": file2[i], "status": "same"})
            else:
                result.append({"name": i, "value": file1[i], "status": "old"})
                result.append({"name": i, "value": file2[i], "status": "new"})

    for i in new_keys:
        if isinstance(file2[i], dict):
            result.append({"name": i, "value": comparing_files(file2[i], file2[i]), "status": "new"})
        else:
            result.append({"name": i, "value": file2[i], "status": "new"})
    
    for i in old_keys:
        if isinstance(file1[i], dict):
            result.append({"name": i, "value": comparing_files(file1[i], file1[i]), "status": "old"})
        else:
            result.append({"name": i, "value": file1[i], "status": "old"})

    return result

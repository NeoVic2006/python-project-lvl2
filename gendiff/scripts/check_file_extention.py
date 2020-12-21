import json
import yaml


def check_extension(file_name1, file_name2):
    '''
    Checking files format and starts proper function
    to convert the files

    Parameters:
       file_name1 = string Name of the first file
       file_name2 = string Name of the first file
    '''

    if file_name1[-4:] == 'json' and file_name2[-4:] == 'json':
        return generate_diff_JSON(file_name1, file_name2)

    elif file_name1[-3:] == 'yml' and file_name2[-3:] == 'yml':
        return generate_diff_YAML(file_name1, file_name2)
    else:
        return print('Files have different formats')


def generate_diff_JSON(json_file_1, json_file_2):
    json1 = json.load(open(json_file_1))
    json2 = json.load(open(json_file_2))
    return json1, json2


def generate_diff_YAML(yml_file_1, yml_file_2):
    yaml1 = yaml.load(open(yml_file_1, 'r'), Loader=yaml.FullLoader)
    yaml2 = yaml.load(open(yml_file_2, 'r'), Loader=yaml.FullLoader)
    return yaml1, yaml2

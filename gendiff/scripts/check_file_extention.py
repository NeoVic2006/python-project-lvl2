from gendiff.gendiff_file import generate_diff_JSON, generate_diff_YAML


def check_extension(file_name1, file_name2):
    print(file_name1, file_name2)
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
        return print('Files have different format')

from operator import itemgetter
from gendiff.check_file_extention import check_extension
from gendiff.formatters.formatter import formatters
from gendiff.formatters.formatter import DEFAULT_STYLE


def generate_diff(file1, file2, format=DEFAULT_STYLE):
    file1 = check_extension(file1)
    file2 = check_extension(file2)
    return formatters(_get_diff(file1, file2), format)


def _get_diff(file1, file2):
    new_keys, old_keys, same_keys = getting_keys(file1, file2)
    result = []
    for key in same_keys:
        if isinstance(file1[key], dict) and isinstance(file2[key], dict):
            result.append({"name": key,
                           "value": _get_diff(file1[key], file2[key]),
                           "status": "same"})
        elif file1[key] == file2[key]:
            result.append({"name": key, "value": file2[key], "status": "same"})
        else:
            result.append({"name": key,
                           "value": file1[key],
                           "status": "changed_old"})
            result.append({"name": key,
                           "value": file2[key],
                           "status": "changed_new"})

    for key in old_keys:
        result.append({"name": key, "value": file1[key], "status": "old"})
    for key in new_keys:
        result.append({"name": key, "value": file2[key], "status": "new"})
    return sorting(result)


def sorting(result):
    return sorted(result, key=itemgetter('name'))


def getting_keys(file1, file2):
    new_keys = file2.keys() - file1.keys()
    old_keys = file1.keys() - file2.keys()
    same_keys = file1.keys() - new_keys - old_keys
    return new_keys, old_keys, same_keys

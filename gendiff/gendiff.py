from operator import itemgetter
from gendiff.scripts.check_file_extention import check_extension
from gendiff.formatters.formatter import formatters


def generate_diff(file1, file2, format="stylish"):
    file1, file2 = check_extension(file1, file2)
    return formatters(_get_diff(file1, file2), format)


def _get_diff(file1, file2):
    new_keys = file2.keys() - file1.keys()
    old_keys = file1.keys() - file2.keys()
    same_keys = file1.keys() - new_keys - old_keys
    result = []
    for key in same_keys:
        if isinstance(file1[key], dict) and isinstance(file2[key], dict):
            result.append({"name": key,
                           "value": _get_diff(file1[key], file2[key]),
                           "status": "same"})
        else:
            if file1[key] == file2[key]:
                result.append(_single_file_check(key, file2, "same"))
            else:
                result.append(_single_file_check(key, file1, "changed_old"))
                result.append(_single_file_check(key, file2, "changed_new"))

    for key in old_keys:
        result.append(_single_file_check(key, file1, "old"))

    for key in new_keys:
        if isinstance(file2[key], dict):
            result.append({"name": key,
                           "value": _tree_for_newvalues(file2[key]),
                           "status": "new"})
        else:
            result.append(_single_file_check(key, file2, "new"))

    result = sorted(result, key=itemgetter('name'))
    return result


def _single_file_check(key, file, status):
    if isinstance(file[key], dict):
        return {"name": key,
                "value": _get_diff(file[key], file[key]),
                "status": status}
    else:
        return {"name": key, "value": file[key], "status": status}


def _tree_for_newvalues(value):
    result = []
    for key in value.keys():
        if isinstance(value[key], dict):
            result.append({"name": key,
                           "value": _tree_for_newvalues(value[key]),
                           "status": "same"})
        else:
            result.append({"name": key, "value": value[key], "status": "same"})
    return result

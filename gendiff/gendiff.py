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
            result.append(status_tree(file2, key, "same", "same"))
        else:
            result.append(status_tree(file1, key, "same", "changed_old"))
            result.append(status_tree(file2, key, "same", "changed_new"))
    for key in old_keys:
        result.append(status_tree(file1, key, "same", "old"))
    for key in new_keys:
        result.append(status_tree(file2, key, "same", "new"))
    return sorting(result)


def sorting(result):
    return sorted(result, key=itemgetter('name'))


def getting_keys(file1, file2):
    new_keys = file2.keys() - file1.keys()
    old_keys = file1.keys() - file2.keys()
    same_keys = file1.keys() - new_keys - old_keys
    return new_keys, old_keys, same_keys


def status_tree(file, key, ins_status, out_status):
    if isinstance(file[key], dict):
        return {"name": key,
                "value": _tree_for_singlevalues(file[key], ins_status),
                "status": out_status}
    else:
        return {"name": key, "value": file[key], "status": out_status}


def _tree_for_singlevalues(value, status):
    result = []
    for key in value.keys():
        if isinstance(value[key], dict):
            result.append({"name": key,
                           "value": _tree_for_singlevalues(value[key], status),
                           "status": status})
        else:
            result.append({"name": key, "value": value[key], "status": status})
    return result

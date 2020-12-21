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
    for i in same_keys:
        if isinstance(file1[i], dict) and isinstance(file2[i], dict):
            result.append({"name": i,
                           "value": _get_diff(file1[i], file2[i]),
                           "status": "same"})
        else:
            if file1[i] == file2[i]:
                result.append(_single_file_check(i, file2, "same"))
            else:
                result.append(_single_file_check(i, file1, "changed_old"))
                result.append(_single_file_check(i, file2, "changed_new"))

    for i in old_keys:
        result.append(_single_file_check(i, file1, "old"))
    for i in new_keys:
        result.append(_single_file_check(i, file2, "new"))
    result = sorted(result, key=itemgetter('name'))
    return result


def _single_file_check(i, file, status):
    if isinstance(file[i], dict):
        return {"name": i,
                "value": _get_diff(file[i], file[i]),
                "status": status}
    else:
        return {"name": i, "value": file[i], "status": status}

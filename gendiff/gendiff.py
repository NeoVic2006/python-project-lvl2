from operator import itemgetter
from gendiff.get_data_from_file import getting_file_data
from gendiff.formatters.formatter import cheking_format
from gendiff.formatters.formatter import DEFAULT_STYLE


def generate_diff(file1, file2, format=DEFAULT_STYLE):
    file1_data = getting_file_data(file1)
    file2_data = getting_file_data(file2)
    return cheking_format(_get_diff(file1_data, file2_data), format)


def _get_diff(file1_data, file2_data):
    new_keys, old_keys, same_keys = getting_keys(file1_data, file2_data)
    result = []
    for key in same_keys:
        if isinstance(file1_data[key], dict) and isinstance(file2_data[key],
                                                            dict):
            result.append({"name": key,
                           "value": _get_diff(file1_data[key],
                                              file2_data[key]),
                           "status": "same"})
        elif file1_data[key] == file2_data[key]:
            result.append({"name": key, "value": file2_data[key],
                           "status": "same"})
        elif isinstance(file1_data[key], dict):
            result.append({"name": key,
                            "value": _get_diff(file1_data[key],
                                                file1_data[key]),
                            "value_new": file2_data[key],
                            "status": "changed"})
        elif isinstance(file2_data[key], dict):
            result.append({"name": key,
                            "value": file1_data[key],
                            "value_new": _get_diff(file2_data[key],
                                                    file2_data[key]),
                            "status": "changed"})
        else:
            result.append({"name": key,
                            "value": file1_data[key],
                            "value_new": file2_data[key],
                            "status": "changed"})
    for key in old_keys:
        if isinstance(file1_data[key], dict):
            result.append({"name": key,
                           "value": _get_diff(file1_data[key],
                                              file1_data[key]),
                           "status": "old"})
        else:
            result.append({"name": key, "value": file1_data[key],
                           "status": "old"})
    for key in new_keys:
        if isinstance(file2_data[key], dict):
            result.append({"name": key,
                           "value": _get_diff(file2_data[key],
                                              file2_data[key]),
                           "status": "new"})
        else:
            result.append({"name": key, "value": file2_data[key],
                           "status": "new"})

    return sorted(result, key=itemgetter('name'))


def getting_keys(file1, file2):
    new_keys = file2.keys() - file1.keys()
    old_keys = file1.keys() - file2.keys()
    same_keys = file1.keys() - new_keys - old_keys
    return new_keys, old_keys, same_keys

from gendiff.gendiff_file import generate_diff

def test_answer():
    result = '{ \n  + verbose: True\n    host: hexlet.io\n  - timeout: 50\n  + timeout: 20\n  - proxy: 123.234.53.22\n  - follow: False\n}'
    assert generate_diff("files/file1.json", "files/file2.json") == result


if __name__ == '__main__':
    test_answer()

# pytest -q files_check_tests.py

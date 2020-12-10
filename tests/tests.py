from gendiff.gendiff_file import generate_diff_JSON, generate_diff_YAML
from gendiff.scripts.check_file_format import check_format

def test_answer():
    result = '{ \n  + verbose: True\n    host: hexlet.io\n  - timeout: 50\n  + timeout: 20\n  - proxy: 123.234.53.22\n  - follow: False\n}'
    assert generate_diff_JSON("tests/fixtures/file1.json", "tests/fixtures/file2.json") == result
    assert generate_diff_YAML("tests/fixtures/filepath1.yml", "tests/fixtures/filepath2.yml") == result
    assert check_format("file1.json", "file2.json") == result


if __name__ == '__main__':
    test_answer()


# pytest -q tests_for_JSON.py
# pip install pytest-cov  
# pytest --cov=gendiff --cov-report xml tests/tests_for_JSON.py

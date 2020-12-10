from gendiff.gendiff_file import generate_diff_JSON


def test_answer():
    result = '{ \n  + verbose: True\n    host: hexlet.io\n  - timeout: 50\n  + timeout: 20\n  - proxy: 123.234.53.22\n  - follow: False\n}'
    assert generate_diff_JSON("tests/fixtures/file1.json", "tests/fixtures/file2.json") == result


if __name__ == '__main__':
    test_answer()

# pytest -q tests_for_JSON.py
# pip install pytest-cov  
# pytest --cov=gendiff --cov-report xml tests/tests_for_JSON.py

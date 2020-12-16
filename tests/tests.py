from gendiff.gendiff_file import generate_diff_JSON, generate_diff_YAML
from gendiff.scripts.formatters import _formatter
from gendiff.scripts.check_file_extention import check_extension


'''
def test_generate_diff_JSON():
    with open("tests/answers/generate_diff_result.txt", "r") as f:
        answer = f.read().strip()
    result = str(generate_diff_JSON("tests/fixtures/json_files/file1.json", "tests/fixtures/json_files/file2.json"))
    assert result == answer


def test_generate_diff_YAML():
    with open("tests/answers/generate_diff_result.txt", "r") as f:
        answer = f.read().strip()
    result = str(generate_diff_YAML("tests/fixtures/yaml_files/file1.yml", "tests/fixtures/yaml_files/file2.yml"))
    assert result == answer
'''

def test_formatter_stylish():
    with open("tests/answers/_formatter_stylish.txt", "r") as f:
        answer = " " + f.read().strip()
    result_JSON_stylish = _formatter(generate_diff_JSON("tests/fixtures/json_files/file1.json", "tests/fixtures/json_files/file2.json"), "stylish")
    result_YAML_stylish = _formatter(generate_diff_YAML("tests/fixtures/yaml_files/file1.yml", "tests/fixtures/yaml_files/file2.yml"), "stylish")
    assert result_JSON_stylish == answer
    assert result_YAML_stylish == answer


def test_check_file_extention():
    with open("tests/answers/generate_diff_result.txt", "r") as f:
        answer = f.read().strip()
    result = str(check_extension("tests/fixtures/json_files/file1.json", "tests/fixtures/json_files/file2.json"))
    result = str(check_extension("tests/fixtures/yaml_files/file1.yml", "tests/fixtures/yaml_files/file2.yml"))
    assert result == answer


if __name__ == '__main__':
    #test_generate_diff_JSON()
    #test_generate_diff_YAML()
    test_formatter_stylish()
    test_check_file_extention()


# pytest -q tests/tests.py
# pip install pytest-cov  
# pytest --cov=gendiff --cov-report xml tests/tests.py

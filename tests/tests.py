from gendiff.gendiff import generate_diff
from gendiff.formatters.formatter import formatters


def test_formatter_stylish():
    with open("tests/answers/_formatter_stylish.txt", "r") as f:
        answer = f.read()
    result_JSON_stylish = formatters(generate_diff("tests/fixtures/json_files/file1.json", "tests/fixtures/json_files/file2.json"), "stylish")
    result_YAML_stylish = formatters(generate_diff("tests/fixtures/yaml_files/file1.yml", "tests/fixtures/yaml_files/file2.yml"), "stylish")
    assert result_JSON_stylish == answer
    assert result_YAML_stylish == answer


def test_formatter_plain():
    with open("tests/answers/_formatter_plain.txt", "r") as f:
        answer = f.read()
    result_JSON_stylish = formatters(generate_diff("tests/fixtures/json_files/file1recursive.json", "tests/fixtures/json_files/file2recursive.json"), "plain")
    result_YAML_stylish = formatters(generate_diff("tests/fixtures/yaml_files/file1recursive.yml", "tests/fixtures/yaml_files/file2recursive.yml"), "plain")
    assert result_JSON_stylish == answer
    assert result_YAML_stylish == answer


def test_formatter_json():
    with open("tests/answers/_formatter_JSON.txt", "r") as f:
        answer = f.read()
    result_JSON_stylish = formatters(generate_diff("tests/fixtures/json_files/file1recursive.json", "tests/fixtures/json_files/file2recursive.json"), "json")
    result_YAML_stylish = formatters(generate_diff("tests/fixtures/yaml_files/file1recursive.yml", "tests/fixtures/yaml_files/file2recursive.yml"), "json")
    assert result_JSON_stylish == answer
    assert result_YAML_stylish == answer


if __name__ == '__main__':
    test_formatter_plain()
    test_formatter_stylish()
    test_formatter_json()


# pytest -q tests/tests.py
# pip install pytest-cov  
# pytest --cov=gendiff --cov-report xml tests/tests.py

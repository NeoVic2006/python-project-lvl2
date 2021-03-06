from gendiff.gendiff import generate_diff
import pytest


@pytest.mark.parametrize("file_path, file1, file2, style", [
    ("tests/fixtures/test_recursive_JSON_YAML/answer.txt", "tests/fixtures/test_recursive_JSON_YAML/file1recursive.json", "tests/fixtures/test_recursive_JSON_YAML/file2recursive.json", "stylish"),
    ("tests/fixtures/test_recursive_JSON_YAML/answer.txt", "tests/fixtures/test_recursive_JSON_YAML/file1recursive.yml", "tests/fixtures/test_recursive_JSON_YAML/file2recursive.yml", "stylish"),
    ("tests/fixtures/test_formatter_json/answer.txt", "tests/fixtures/test_formatter_json/file1recursive.json", "tests/fixtures/test_formatter_json/file2recursive.json", "json"),
    ("tests/fixtures/test_formatter_json/answer.txt", "tests/fixtures/test_formatter_json/file1recursive.yml", "tests/fixtures/test_formatter_json/file2recursive.yml", "json"),
    ("tests/fixtures/test_formatter_plain/answer.txt", "tests/fixtures/test_formatter_plain/file1recursive.json", "tests/fixtures/test_formatter_plain/file2recursive.json", "plain"),
    ("tests/fixtures/test_formatter_plain/answer.txt", "tests/fixtures/test_formatter_plain/file1recursive.yml", "tests/fixtures/test_formatter_plain/file2recursive.yml", "plain"),
    ("tests/fixtures/test_formatter_stylish/answer.txt", "tests/fixtures/test_formatter_stylish/file1.json", "tests/fixtures/test_formatter_stylish/file2.json", "stylish"),
    ("tests/fixtures/test_formatter_stylish/answer.txt", "tests/fixtures/test_formatter_stylish/file1.yml", "tests/fixtures/test_formatter_stylish/file2.yml", "stylish"), ])
def test_eval(file_path, file1, file2, style):
    with open(file_path, "r") as f:
        answer = f.read()
    assert answer == generate_diff(file1, file2, style)

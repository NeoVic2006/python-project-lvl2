from gendiff.gendiff import generate_diff


def test_formatter_stylish():
    with open("tests/fixtures/test_formatter_stylish/answer.txt", "r") as f:
        answer = f.read()
    result_JSON_stylish = generate_diff("tests/fixtures/test_formatter_stylish/file1.json", "tests/fixtures/test_formatter_stylish/file2.json", "stylish")
    result_YAML_stylish = generate_diff("tests/fixtures/test_formatter_stylish/file1.yml", "tests/fixtures/test_formatter_stylish/file2.yml", "stylish")
    assert result_JSON_stylish == answer
    assert result_YAML_stylish == answer


def test_formatter_plain():
    with open("tests/fixtures/test_formatter_plain/answer.txt", "r") as f:
        answer = f.read()
    result_JSON_plain = generate_diff("tests/fixtures/test_formatter_plain/file1recursive.json", "tests/fixtures/test_formatter_plain/file2recursive.json", "plain")
    result_YAML_plain = generate_diff("tests/fixtures/test_formatter_plain/file1recursive.yml", "tests/fixtures/test_formatter_plain/file2recursive.yml", "plain")
    assert result_JSON_plain == answer
    assert result_YAML_plain == answer


def test_formatter_json():
    with open("tests/fixtures/test_formatter_json/answer.txt", "r") as f:
        answer = f.read()
    result_JSON_json = generate_diff("tests/fixtures/test_formatter_json/file1recursive.json", "tests/fixtures/test_formatter_json/file2recursive.json", "json")
    result_YAML_json = generate_diff("tests/fixtures/test_formatter_json/file1recursive.yml", "tests/fixtures/test_formatter_json/file2recursive.yml", "json")
    assert result_JSON_json == answer
    assert result_YAML_json == answer


def test_recursive_JSON_YAML():
    with open("tests/fixtures/test_recursive_JSON_YAML/answer.txt", "r") as f:
        answer = f.read()
    result_JSON = generate_diff("tests/fixtures/test_recursive_JSON_YAML/file1recursive.json", "tests/fixtures/test_recursive_JSON_YAML/file2recursive.json", "stylish")
    result_YAML = generate_diff("tests/fixtures/test_recursive_JSON_YAML/file1recursive.yml", "tests/fixtures/test_recursive_JSON_YAML/file2recursive.yml", "stylish")
    assert result_JSON == answer
    assert result_YAML == answer


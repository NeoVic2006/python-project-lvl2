from gendiff.gendiff import generate_diff


def test_formatter_stylish():
    with open("tests/answers/_formatter_stylish.txt", "r") as f:
        answer = f.read()
    result_JSON_stylish = generate_diff("tests/fixtures/json_files/file1.json", "tests/fixtures/json_files/file2.json", "stylish")
    result_YAML_stylish = generate_diff("tests/fixtures/yaml_files/file1.yml", "tests/fixtures/yaml_files/file2.yml", "stylish")
    assert result_JSON_stylish == answer
    assert result_YAML_stylish == answer


def test_formatter_plain():
    with open("tests/answers/_formatter_plain.txt", "r") as f:
        answer = f.read()
    result_JSON_plain = generate_diff("tests/fixtures/json_files/file1recursive.json", "tests/fixtures/json_files/file2recursive.json", "plain")
    result_YAML_plain = generate_diff("tests/fixtures/yaml_files/file1recursive.yml", "tests/fixtures/yaml_files/file2recursive.yml", "plain")
    assert result_JSON_plain == answer
    assert result_YAML_plain == answer


def test_formatter_json():
    with open("tests/answers/_formatter_JSON.txt", "r") as f:
        answer = f.read()
    result_JSON_json = generate_diff("tests/fixtures/json_files/file1recursive.json", "tests/fixtures/json_files/file2recursive.json", "json")
    result_YAML_json = generate_diff("tests/fixtures/yaml_files/file1recursive.yml", "tests/fixtures/yaml_files/file2recursive.yml", "json")
    assert result_JSON_json == answer
    assert result_YAML_json == answer


def test_recursive_JSON_YAML():
    with open("tests/answers/recursive_JSON_YAML.txt", "r") as f:
        answer = f.read()
    result_JSON = generate_diff("tests/fixtures/json_files/file1recursive.json", "tests/fixtures/json_files/file2recursive.json", "stylish")
    result_YAML = generate_diff("tests/fixtures/yaml_files/file1recursive.yml", "tests/fixtures/yaml_files/file2recursive.yml", "stylish")
    assert result_JSON == answer
    assert result_YAML == answer

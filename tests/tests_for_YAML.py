from gendiff.gendiff_file import generate_diff_YAML


def test_answer():
    result = '{ \n  + verbose: True\n    host: hexlet.io\n  - timeout: 50\n  + timeout: 20\n  - proxy: 123.234.53.22\n  - follow: False\n}'
    assert generate_diff_YAML("fixtures/filepath1.yml", "fixtures/filepath2.yml") == result





# pytest -q generate_diff_YAML.py

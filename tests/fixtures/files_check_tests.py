import json
import os
from gendiff.gendiff_file import generate_diff

def test_answer():

    path = os.getcwd()
    print(path)

    '''
    file_path1 = json.load(open('/home/runner/work/python-project-lvl2/python-project-lvl2/tests/fixtures/files/file1.json'))
    file_path2 = json.load(open('/home/runner/work/python-project-lvl2/python-project-lvl2/tests/fixtures/files/file2.json'))
    
    # Ubuntu version
    file_path1 = json.load(open('/mnt/c/Python_Work_for_Hexlet/python-project-lvl2/tests/fixtures/files/file1.json'))
    file_path2 = json.load(open('/mnt/c/Python_Work_for_Hexlet/python-project-lvl2/tests/fixtures/files/file2.json'))
    
    # CMD version 
    file_path1 = json.load(open('files/file1.json'))
    file_path2 = json.load(open('files/file2.json'))
    '''

    result = '{ \n  + verbose: True\n    host: hexlet.io\n  - timeout: 50\n  + timeout: 20\n  - proxy: 123.234.53.22\n  - follow: False\n}'
    assert generate_diff("files/file1.json", "files/file2.json") == result


if __name__ == '__main__':
    test_answer()

# pytest -q files_check_tests.py
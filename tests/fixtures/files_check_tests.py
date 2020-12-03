import json
from files_check import generate_diff


def test_answer():

    '''
    # Ubuntu version
    file_path1 = json.load(open('/mnt/c/Python_Work_for_Hexlet/files/file1.json'))
    file_path2 = json.load(open('/mnt/c/Python_Work_for_Hexlet/files/file2.json'))
    '''
    
    # CMD version 
    file_path1 = json.load(open('C:\\Python_Work_for_Hexlet\\files\\file1.json'))
    file_path2 = json.load(open('C:\\Python_Work_for_Hexlet\\files\\file2.json'))
    
    

    result = '{ \n  + verbose: True\n    host: hexlet.io\n  - timeout: 50\n  + timeout: 20\n  - proxy: 123.234.53.22\n  - follow: False\n}'
    assert generate_diff(file_path1, file_path2) == result


if __name__ == '__main__':
    pass

    
test_answer()

# pytest -q files_check_tests.py
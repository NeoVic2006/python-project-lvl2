import argparse
import json


def main():
    parser = argparse.ArgumentParser(description="Generate diff")
    parser.add_argument("first_file")
    parser.add_argument("second_file")
    parser.add_argument("-f","--format", help="set format of output")
    args = parser.parse_args()
    return print(args.echo)

'''
file_path1 = json.load(open('C:\Python_Work_for_Hexlet\python-project-lvl2\\files\\file1.json'))


def generate_diff(file_path1):
    print(file_path1)



generate_diff(file_path1)
'''
if __name__ == '__main__':
    main()





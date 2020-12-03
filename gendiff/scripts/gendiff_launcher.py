import argparse
import json
from os import path
import os
from gendiff import generate_diff


def main():
    parser = argparse.ArgumentParser(description="New Generated diff")
    parser.add_argument("first_file")
    parser.add_argument("second_file")
    parser.add_argument("-f", "--format", help="set format of output")
    args = parser.parse_args()
    cheking_files(args)
    return args


def cheking_files(args):
    if str(path.exists(args.first_file)) is False:
        print("File 1 is not found!")
        return
    if str(path.exists(args.second_file)) is False:
        print("File 2 is not found!")
        return
    my_absolute_dirpath = os.path.abspath(os.path.dirname(__file__))
    file_path1 = json.load(open(my_absolute_dirpath + '/' + args.first_file))
    file_path2 = json.load(open(my_absolute_dirpath + '/' + args.second_file))
    result = generate_diff(file_path1, file_path2)
    print(result)


if __name__ == '__main__':
    main()

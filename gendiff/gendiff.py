import argparse
import json
from os import path
import os
from files_check import generate_diff

def main():
    
    parser = argparse.ArgumentParser(description="New Generated diff")
    parser.add_argument("first_file")
    parser.add_argument("second_file")
    parser.add_argument("-f", "--format", help="set format of output")
    args = parser.parse_args()
    cheking_files(args)
    return args


def cheking_files(args):
    print ("File 1 exists:"+str(path.exists(args.first_file)))
    print ("File 2 exists:"+str(path.exists(args.second_file)))  

    my_absolute_dirpath = os.path.abspath(os.path.dirname(__file__))
    file_path1 = json.load(open(my_absolute_dirpath + '/' + args.first_file))
    file_path2 = json.load(open(my_absolute_dirpath + '/' + args.second_file))
    result = generate_diff(file_path1, file_path2)
    print(result)
    return


if __name__ == '__main__':
    main()


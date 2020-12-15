import argparse
from gendiff.scripts.check_file_format import check_format
from .stylish import stylish


def main():
    '''
    Main script. Starts library gendiff.
    For more info type "gendiff -h"
    Returns the result of comparing the two files.
    '''
    parser = argparse.ArgumentParser(description="New Generated diff")
    parser.add_argument("first_file")
    parser.add_argument("second_file")
    parser.add_argument("-f", "--format", help="set format of output")
    args = parser.parse_args()
    stylish_format = stylish(check_format(args.first_file, args.second_file))
    print(stylish_format)
    return stylish_format


if __name__ == '__main__':
    main()

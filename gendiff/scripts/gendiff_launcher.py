import argparse
from gendiff.scripts.check_file_extention import check_extension
from gendiff.scripts.formatters import formatter


def main():
    '''
    Main script. Starts library gendiff.
    For more info type "gendiff -h"
    Returns the result of comparing the two files.
    '''
    parser = argparse.ArgumentParser(description="New Generated diff")
    parser.add_argument("first_file")
    parser.add_argument("second_file")
    parser.add_argument("-f", "--format",
                        help="set output format",
                        default="stylish")
    args = parser.parse_args()
    print(check_extension(args.first_file,args.second_file), args.format)
    result = formatter(check_extension(args.first_file,
                                       args.second_file), args.format)
    print(result)
    # test
    return result


if __name__ == '__main__':
    main()

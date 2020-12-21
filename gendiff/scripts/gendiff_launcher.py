import argparse
from gendiff.gendiff import generate_diff
from gendiff.formatters.formatter import formatters


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
    result = formatters(generate_diff(args.first_file,
                                      args.second_file), args.format)
    print(result)
    return result


if __name__ == '__main__':
    main()

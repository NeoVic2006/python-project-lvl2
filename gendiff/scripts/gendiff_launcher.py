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
    result = check_format(args.first_file, args.second_file)
    #print(result)
    final_result = stylish(result)
    print(final_result)
    return final_result


if __name__ == '__main__':
    main()

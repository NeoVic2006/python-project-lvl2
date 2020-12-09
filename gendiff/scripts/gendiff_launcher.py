import argparse
from gendiff.gendiff_file import generate_diff


def main():
    parser = argparse.ArgumentParser(description="New Generated diff")
    parser.add_argument("first_file")
    parser.add_argument("second_file")
    parser.add_argument("-f", "--format", help="set format of output")
    args = parser.parse_args()
    print(type(args.first_file))
    result = generate_diff(args.first_file, args.second_file)
    print(result)
    return result


if __name__ == '__main__':
    main()

import argparse

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("echo")

    args = parser.parse_args()


    return print(args.echo)



if __name__ == '__main__':
    main()





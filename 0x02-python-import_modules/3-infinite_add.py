#!/usr/bin/python3

if __name__ == "__main__":
    from sys import argv

    len = len(argv)

    result = 0

    for i in range(1, len):
        result += int(argv[i])
    print(result)

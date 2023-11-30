#!/usr/bin/python3
from sys import argv, exit

if __name__ == '__main__':
    argc = len(argv)
    if argc == 1:
        print("0 arguments.")
        exit()

    arg = "arguments" if argc > 2 else "argument"
    print("{} {}:".format(argc - 1, arg))
    for i in range(1, argc):
        print("{}: {}".format(i, argv[i]))
else:
    exit()

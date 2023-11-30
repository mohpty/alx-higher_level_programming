#!/usr/bin/python3
from sys import argv, exit

if __name__ == '__main__':
    nums = argv[1:]
    print(sum(list(map(int, nums))))

else:
    exit()

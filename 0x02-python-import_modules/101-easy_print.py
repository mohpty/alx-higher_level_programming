#!/usr/bin/python3
from os import write
if __name__ == '__main__':
    write(1, "#pythoniscool".encode('utf-8') + b'\n')

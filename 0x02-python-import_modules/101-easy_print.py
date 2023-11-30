#!/usr/bin/python3
from os import write

text = "#pythoniscool"
descriptor = 1
write(1, text.encode('utf-8') + b'\n')

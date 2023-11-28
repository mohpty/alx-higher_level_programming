#!/usr/bin/python3
z = 0
for i in range(26):
    if z:
        print("{}".format(chr(90 - i)), end='')
    else:
        print("{}".format(chr(122 - i)), end='')
    z = not z

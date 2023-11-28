#!/usr/bin/python3
def pow(a, b):
    x = 1
    if b == 0:
        pass
    elif b > 0:
        for i in range(b):
            x *= a
    else:
        for i in range(b * -1):
            x *= a
        x = 1 / x

    return x

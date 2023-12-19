#!/usr/bin/python3

def safe_print_division(a, b):
    try:
        safe = a / b
    except ZeroDivisionError:
        print("Inside result: {}".format(None))
    else:
        print("Inside result: {}".format(result))
        return safe
    finally:
        pass

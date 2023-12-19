#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    try:
        con = fct(*args)
        return con
    except Exception as e:
        print("Exception:", e, file=sys.stderr)
        return None

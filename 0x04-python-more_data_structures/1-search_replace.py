#!/usr/bin/python3
def search_replace(my_list, search, replace):
    out = my_list[:]
    for i in range(len(out)):
        if out[i] == search:
            out[i] = replace
            break
    return out

#!/usr/bin/python3
def search_replace(my_list, search, replace):
    out = []
    for item in my_list:
        if item == search:
            out.append(replace)
        else:
            out.append(item)
    return out

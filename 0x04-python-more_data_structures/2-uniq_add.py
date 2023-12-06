#!/usr/bin/python3
def uniq_add(my_list=[]):
    out = []
    uniq = {i: 0 for i in my_list}
    for i in my_list:
        if uniq[i] == 0:
            out.append(i)
            uniq[i] = 1
        else:
            pass
    return sum(out)

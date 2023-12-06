#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    tobedel = []
    if value == None or a_dictionary == None:
        return a_dictionary
    for k, v in a_dictionary.items():
        if v == value:
            tobedel.append(k)
        else:
            pass
    for i in tobedel:
        del a_dictionary[i]

    return a_dictionary

#!/usr/bin/python3
def weight_average(my_list=[]):
    if len(my_list) == 0:
        return 0
    weight_total = 0
    total = 0
    for pair in my_list:
        total += pair[0] * pair[1]
        weight_total += pair[1]
    return total / weight_total

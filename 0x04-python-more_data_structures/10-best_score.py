#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary:
        arr = list(a_dictionary.keys())
        val = 0
        mx = ""
        for i in arr:
            if arr[i] > val:
                val = a_dictionary[i]
                mx = i
        return mx

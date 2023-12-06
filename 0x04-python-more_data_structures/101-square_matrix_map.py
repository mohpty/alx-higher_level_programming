#!/usr/bin/python3
def square_matrix_map(matrix=[]):
    out = matrix[:]
    for i in range(len(out)):
        out[i] = list(map(lambda x: x * x, out[i]))
    return out

#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    out = [matrix[i][:] for i in range(len(matrix))]
    for i in range(len(out)):
        for j in range(len(out[i])):
            out[i][j] *= out[i][j]
    return out

import numpy as np


def matrix_generator(n):
    matrix = []
    for i in range(n):
        line = []
        for j in range(n):
            line.append(np.random.randint(1, 10))
        matrix.append(line)
    return matrix


# @np.vectorize
def maxmin(matrix):
    print(matrix)
    numbers = []
    for i in range(3):
        numbers.append(max(matrix[i]))
    print(min(numbers))


maxmin(matrix_generator(3))

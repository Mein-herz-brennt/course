import numpy as np


def matrix_generator(n):
    matrix = []
    for i in range(n):
        line = []
        for j in range(n):
            line.append(np.random.randint(1, 6))
        matrix.append(line)
    return matrix


# @np.vectorize
def magic(matrix):
    print(matrix)
    numbers = []
    nums = []
    for i in range(3):
        num = 0
        numbers.append(matrix[i][0] + matrix[i][1] + matrix[i][2])
        for j in range(3):
            num += matrix[j][i]
        nums.append(num)
    for i in range(len(numbers)):
        if numbers[i] != nums[i]:
            print("матриця не є магічним квадратом")
            break
    else:
        print("Матриця є магічним квадратом")


magic(matrix_generator(3))
matr = [[1, 1, 1], [1, 1, 1], [1, 1, 1]]
magic(matr)

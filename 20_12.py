import numpy as np


def matrix_generator(n):
    matrix = []
    for i in range(n):
        line = []
        for j in range(n):
            line.append(np.random.randint(0, 1))
        matrix.append(line)
    return matrix


# @np.vectorize
def magic(matrix, v):
    print(matrix)
    nums = []
    if v == "up":
        for i in range(len(matrix)):
            for j in range(len(matrix[i]) - 1):
                if matrix[i][j] == 0 and matrix[i][len(matrix) - 1] != 0:
                    nums.append(1)
                else:
                    nums.append(0)
            print(nums)
        if nums[0] == 1 and nums[1] == 1 and nums[2] == 1:
            print("матриця є верхньою трикутною")
        else:
            print("матриця не є верхньою трикутною")
    elif v == "down":
        for i in range(len(matrix)):
            if matrix[i][0] != 0 and matrix[i][1] == 0 and matrix[i][2] == 0:
                nums.append(1)
            elif matrix[i][0] != 0 and matrix[i][1] != 0 and matrix[i][2] == 0:
                nums.append(1)
            else:
                nums.append(0)
        print(nums)
        if nums[1] == 1 and nums[2] == 1:
            print("матриця є нижньою  трикутною")
        else:
            print("матриця не є нижньою трикутною")


matr = [[1, 1, 1], [1, 1, 0], [1, 0, 0]]
magic(matr, "down")

# magic(matrix_generator(3))

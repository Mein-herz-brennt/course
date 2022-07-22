from random import randint


def matrix_generator(n):  # n - розмірність матриці, матриця завжди квадратна
    matrix = []
    for i in range(n):
        line = []
        for j in range(n):
            line.append(randint(0, 1))
        matrix.append(line)
    return matrix


def result_generator(n):
    result = []
    for i in range(n):
        line = []
        for j in range(n):
            line.append(0)
        result.append(line)
    return result


def decor(fun):
    def _matrix(*args):
        matrix = fun(*args)
        persent = (len(matrix) * 2) / 100
        slovar = {}
        count = 0
        for i in matrix:
            for j in i:
                if j == 0:
                    count += 1
                else:
                    slovar[f"цифра{j}"] = j
        persents = ((len(matrix) * 2) - count) * persent
        if persents > 0.1:
            return matrix
        else:
            return slovar
    return _matrix


@decor
def sum_matrix(x, y):
    result = result_generator(len(x))
    for i in range(len(x)):
        for j in range(len(x[0])):
            result[i][j] = x[i][j] + y[i][j]
    return result


x = matrix_generator(2)
y = matrix_generator(2)
c = sum_matrix(x, y)
print(c)

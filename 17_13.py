from random import randint

matr = {"1 3": 1,  #
        "3 3": 1,  # матриця в вигляді словника
        "1 2": 1, }  #


# створюмо матрицю у вигляді списку списків
def matrix_g(n):  # n - розмірність матриці, матриця завжди квадратна
    mat = []
    for i in range(n):
        l = []
        for j in range(n):
            l.append(randint(0, 1))
        mat.append(l)
    return mat


# створюємо матрицю всіма елементами якої є нулі в неї будемо записувати результат додавання
def result_g(n):
    res = []
    for i in range(n):
        l = []
        for j in range(n):
            l.append(0)
        res.append(l)
    return res


# декоратор який переводить матрицю словник до  вигляду списку списків
def dec(fun):
    def _matr(*args):
        if str(type(args[0])) == "<class 'dict'>":
            res = result_g(3)
            for keys, item in args[0].items():
                k = keys.split(" ")
                res[int(k[0]) - 1][int(k[1]) - 1] = item
            a = list(args)
            a[0] = res
            return fun(a[0], a[1])
        elif str(type(args[1])) == "<class 'dict'>":
            res = result_g(3)
            for keys, item in args[1].items():
                k = keys.split(" ")
                res[int(k[0]) - 1][int(k[1]) - 1] = item
            a = list(args)
            a[1] = res
            return fun(a[0], a[1])
        else:
            return fun(*args)

    return _matr


@dec
# функція яка додає матриці
def sum_m(x, y):
    res = result_g(len(x))
    for i in range(len(x)):
        for j in range(len(x[0])):
            res[i][j] = x[i][j] + y[i][j]
    return res


# виклики
a = matrix_g(3)
y = matrix_g(3)

print(sum_m(a, matr))
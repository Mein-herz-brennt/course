def get_matr_from_file(filename):
    with open(filename, "r") as file:
        matrix = file.readlines()
    return matrix


def preobraz(matr):
    for i in range(len(matr)):
        matr[i] = matr[i].replace("\n", "").split(" ")
        matr[i] = [int(item) for item in matr[i]]
    return matr


def proverka(l):
    count = len(l)
    for i in l:
        if len(i) != count:
            print("Проверка не удалась, матрица не квадратная")
            break
    return count


def matmult(a, b):
    zip_b = zip(*b)
    zip_b = list(zip_b)
    return [[sum(ele_a * ele_b for ele_a, ele_b in zip(row_a, col_b))
             for col_b in zip_b] for row_a in a]


def check():
    a = [[], [], []]
    matritsa1 = preobraz(get_matr_from_file("matrix1"))
    matritsa2 = preobraz(get_matr_from_file("matrix2"))
    matritsa3 = preobraz(get_matr_from_file("matrix3"))
    if proverka(matritsa1) == proverka(matritsa2) == proverka(matritsa3):
        matr1 = matmult(matritsa1, matritsa2)
        matr2 = matmult(matritsa1, matritsa3)
        matr3 = matmult(matritsa2, matritsa3)
        for i in range(len(matritsa1)):
            for j in range(len(matritsa1[i])):
                if matr3[i][j] == matritsa1[i][j]:
                    a[0].append(1)
        for i in range(len(matritsa2)):
            for j in range(len(matritsa2[i])):
                if matr2[i][j] == matritsa2[i][j]:
                    a[1].append(2)
        for i in range(len(matritsa3)):
            for j in range(len(matritsa3[i])):
                if matr1[i][j] == matritsa3[i][j]:
                    a[2].append(3)

    if len(a[0]) == 9:
        print("Матриця 1 є добутком 2 інших")
    elif len(a[1]) == 9:
        print("Матриця 2 є добутком 2 інших")
    elif len(a[2]) == 9:
        print("Матриця 3 є добутком 2 інших")
    else:
        print("Жодна з матриць не є добутком 2 інших")


check()

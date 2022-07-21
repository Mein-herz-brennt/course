import copy, numpy
from tkinter import *
import sys

root = Tk()
ent1 = Entry()
ent1.grid(column=2, row=1)
lbl1 = Label(text='x + ')
lbl1.grid(column=3, row=1)
ent2 = Entry()
ent2.grid(column=4, row=1)
lbl2 = Label(text=' y = ')
lbl2.grid(column=5, row=1)
ent3 = Entry()
ent3.grid(column=6, row=1)

ent4 = Entry()
ent4.grid(column=2, row=2)
lbl3 = Label(text='x + ')
lbl3.grid(column=3, row=2)
ent5 = Entry()
ent5.grid(column=4, row=2)
lbl5 = Label(text=' y = ')
lbl5.grid(column=5, row=2)
ent6 = Entry()
ent6.grid(column=6, row=2)

lbl6 = Label()
lbl7 = Label()
lbl6.grid(column=3, row=3)
lbl7.grid(column=4, row=3)


# [ent1.get()+'.', ent2.get(), ent3.get(),4],
#                      [ent4.get(), ent5.get(), ent6.get(),5],
#                      [1,2,3,4]])

def gaussFunc():
    a = numpy.array([[int(ent1.get()), int(ent2.get()), int(ent3.get())],
                     [int(ent4.get()), int(ent5.get()), int(ent6.get())]])

    # В метод передавайте вещественный массив))
    eps = 1e-16

    c = numpy.array(a)  # с нам еще понадобится
    a = numpy.array(a)  # создаем копию массива a, используя библиотеку NumPy
    # (зачем? Python-язык с динамической типизацией,
    # приходящий а-любой объект, а мы должны попытаться кастануть его в массив )

    len1 = len(a[:, 0])  # хранит размер матрицы A, то есть n
    print(len1)
    len2 = len(a[0, :])  # n+1
    print(len2)
    # vectB = copy.deepcopy(a[:, len1])#вектор B в Ax=B

    for g in range(len1):

        max = abs(a[g][g])  # переменная для сохранения
        my = g  # максимума в текущем столбце
        t1 = g  # g
        while t1 < len1:  # цикл поиска максимума в столбце g
            if abs(a[t1][g]) > max:
                max = abs(a[t1][g])
                my = t1
            t1 += 1

        if abs(max) < eps:  # Если найденный максимум < 0(машинного) выбрасываем ошибку
            raise DetermExeption("Check determinant")  # тк определитель матрицы равен нулю

        if my != g:
            a[g][:], a[my][:] = a[my][:], a[g][:]  # меняем текущую строку со строкой, в которой
            # максимум (красивая реализация swap(), да?)

        amain = float(a[g][g])  # коэффицент перед текущим x на диагонали

        z = g
        while z < len2:  # делим всю строку на amain коэффицент перед текущим
            a[g][z] = a[g][z] / amain  # x становится  1
            z += 1
        j = g + 1

        while j < len1:  # отнимаем строку, умноженную на коэффицент
            b = a[j][g]  # от следующей, в результате получаем столбец нулей.
            z = g  # Глобальный цикл выполняется до тех пор, пока
            while z < len2:  # не получатся нули в нижней треугольной матрице
                a[j][z] = a[j][z] - a[g][z] * b
                z += 1
            j += 1

    a = back_trace(a, len1)  # обратный ход метода Гаусса

    # print("Погрешность:")
    # print(vectorN(c, a, len1))
    vectorN(c, a, len1)
    # вывод нормы вектора невязки
    return a


class DetermExeption(Exception):  # Ошибка, проверьте определитель матрицы
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return repr(self.value)


def back_trace(a, len1):  # обратный ход
    a = numpy.array(a)
    i = len1 - 1
    while i > 0:
        j = i - 1
        while j >= 0:
            a[j][len1] = a[j][len1] - a[j][i] * a[i][len1]
            j -= 1
        i -= 1
    return a[:, len1]


def vectorN(c, a, len1):  # c-начальная матрица a-ответ len1-кол столбцов, vectB-вектор B
    c = numpy.array(c)
    a = numpy.array(a)
    vectB = copy.deepcopy(c[:, len1])
    b = numpy.zeros((len1))
    i = 0

    while i < len1:  # подставляем полученные x-ы, в матрицу, получаем вектор невязки
        j = 0
        while j < len1:
            b[i] += c[i][j] * a[j]
            j += 1
        i = i + 1

    c = copy.deepcopy(b)

    for i in range(len1):
        c[i] = abs(c[i] - vectB[i])  # отнимаем от вектора невязки вектор B
        # получаем норму
    lbl6['text'] = 'x = {}'.format(a[0])
    lbl7['text'] = 'y = {}'.format(a[1])
    print(a)
    return c


but = Button(text='Обчислити', command=gaussFunc)
but.grid(column=0, row=4)
but1 = Button(text='Вихід', command=sys.exit)
but1.grid(column=6, row=4)

root.mainloop()

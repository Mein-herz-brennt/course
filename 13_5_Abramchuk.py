from math import *
# ВИБАЧТЕ ЩО НЕ ЗАКОМЕНТУВАВ!
a = list(open('numb.txt', 'r'))
A = a
b = ''
for i in A: b += i
b = b.split(' ')
B = []
for i in b:
    B.append(int(i))
AA = []
aa = []
count = 0


def parka(q, count):
    for i in q:
        if i % 2 == 0:
            count += 1
            AA.append(i)
        else:
            aa.append(i)
    return count


Parochka = parka(B, count)
maxmin = max(AA)-min(aa)
print(Parochka, 'Парних числа')
print(maxmin, 'Різниця')
Kvadr = 0


def isint(s):
    try:
        int(s)
        return True
    except ValueError:
        return False


def kvadrat(P, K):
    for i in P:
        a = sqrt(i)
        q = int(a % 1 * 10)
        if a % 2 != 0 and q == 0:
            K += 1
    return K


print(kvadrat(B, Kvadr), 'Квадрати')


def kilkist(g):
    prev = -1
    save = 0
    for i in range(len(g)):
        if i == len(g) - 1:
            break
        elif g[i + 1] == g[i] + 1:
            prev += 1
        else:
            if prev > save:
                save = prev
            else:
                save = save
    return save


print(kilkist(B), 'Кількість членів найдовшої зростаючої послідовності')

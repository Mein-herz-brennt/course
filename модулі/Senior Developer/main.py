from random import randint
from employee import *

r = {}

# 0 - офісний 'планктон' чи тестувальник 
# 1 - junior
# 2 - middle
# 3 - senior

founders = []

for i in range(50):
    a = randint(1, 3)
    q = randint(0, 3)
    b = randint(1, 30)
    d = randint(1, 15)
    w = randint(1, 5)
    s = randint(2500, 3500)
    if a == 1:
        f = Software_engineer(a, q, b, d, w, s, r).calculatesalary()
    elif a == 2:
        f = Offiсe_rat(a, q, b, d, w, s, r).calculatesalary()
    elif a == 3:
        f = Tester(a, q, b, d, w, s, r).calculatesalary()
    founders.append(f)

k = sum(founders)
print('cума заробітних плат всіх працівників:' + str(k))
pod = (k/100) *20
print('податок складає:' + str(pod))
ss = k + pod
print('загальна сума виплат компанією за місяць склала:' + str(ss))

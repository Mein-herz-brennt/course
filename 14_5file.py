from math import *

print('Введіть коефіцієнти рівняння(а,b,c) : ')
coefficient_1, coefficient_2, coefficient_3 = [int(d) for d in input().split()]

print('Введіть степінь рівняння : ')
n = int(input())
assert n == 2


# ax^n+bx+c=0
def function_q2(power, a, b, c):
    if a and b and c != 0:
        discriminant = (b ** 2) - (4 * a * c)

        if discriminant == 0:
            x = (-b) / (2 * a)
            print(x)
        elif discriminant < 0:
            print('Рівняння не має розв\'язків')
        else:
            x_1 = (-b + sqrt(discriminant)) / (2 * a)
            x_2 = (-b - sqrt(discriminant)) / (2 * a)
            print(x_1, x_2)
        # bx+c=0
    elif a == 0 and b != 0 and c != 0:
        x = -c / b
        print(x)
        # ax^2+c=0
    elif b == 0 and a != 0 and c != 0:
        if -c / a >= 0:
            x = sqrt(-c / a)
            print('+-' + str(x))
        else:
            print("Рівняння має розв'язки лише серед комплексних чисел!")
        # ax^2+bx=0
    elif c == 0 and b != 0 and a != 0:
        x_1 = 0
        x_2 = -b / a
        print(x_1, x_2)
    elif a == 0 and b == 0 and c != 0:
        x = -c
        print(x)


# випадки де b і с == 0 а != 0, а і с == 0 b != 0 , та ще багато інших не розглядаю адже на мою думку я розглянув
# випадки що зустрічаються найчастіше
print(function_q2(n, coefficient_1, coefficient_2, coefficient_3))

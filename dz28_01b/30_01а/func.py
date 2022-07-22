def func(x, eps):
    assert abs(x) < 1
    assert eps > 0
    summ = 1
    counter = 1
    a = x
    dodanok = 1
    while abs(dodanok) >= eps:
        summ += pow(-a, counter)
        dodanok = pow(a, counter)
        counter += 1
        # print(summ)
    return summ


# print(func(0.5, 0.0001))

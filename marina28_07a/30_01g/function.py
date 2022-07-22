def func(x, exp):
    assert abs(x) < 1
    assert exp > 0
    x = x
    a = x
    numerator = 1
    n = 1
    summ = 1
    while a > exp:
        numerator *= (2*n - 1)/(2*n)
        a = pow(-x, n)
        summ += numerator*a
        n += 1
    return summ




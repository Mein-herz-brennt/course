def func(x, exp):
    assert abs(x) < 1
    assert exp > 0
    a = x
    x = x
    counter = 1
    summ = 1
    while a > exp:
        a = pow(-1, counter) * pow(x, 2 * counter)
        summ += a
        counter += 1
    return summ








def function(x, exp):
    assert abs(x) < 1
    assert exp > 0
    x = x
    a = x
    summ = 0
    count = 1
    while a > exp:
        a = pow(x, 2 * count - 1)/(2*count - 1)
        summ += a
        count += 1
    return summ * 2

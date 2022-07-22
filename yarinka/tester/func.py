def func(x, eps):
    assert abs(x) < 1
    assert eps > 0
    x = x
    a = x
    counter = 1
    summ = 1
    while abs(a) > eps:
        a = (((counter + 1)*(counter + 2))/2) * pow(-x, counter)
        summ += a
        counter += 1
    return summ


if __name__ == '__main__':
    print(func(0.5, 0.1))

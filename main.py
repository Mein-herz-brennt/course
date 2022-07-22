def generate_dodanky(x):
    x = x
    n = 1
    dodanok = 1
    while True:
        yield dodanok
        dodanok *= pow(-1, n) * ((2*n + 1)/2*n) * pow(x, n)

def check(x, eps):
    assert abs(x) < 1
    assert eps > 0
    x = x
    summ = 0
    for i in generate_dodanky(x):
        if abs(i) >= eps:
            summ += i
    return summ



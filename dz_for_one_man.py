def logger(f):
    def logering(*args, **kwargs):
        a = f.__name__
        if len(kwargs) == 0:
            print(a + " called with args: " + str(*args) + " and kwargs: " + str(kwargs))
        else:
            c = []
            for key, item in kwargs.items():
                c.append("".join(f"{key}='{item}'"))
            b = ",".join(c)
            print(a + " called with args: " + str(*args) + " and kwargs: " + b)
        return f(*args, **kwargs)
    return logering


@logger
def test_some1(a):
    return a


@logger
def test_some2(a, b, c):
    return a


print(test_some1(1))  # test_some1 called with args: 1 and kwargs: {}

print(test_some2(2, b='y',  c='e'))  # test_some2 called with args: 2 and kwargs: b='y',c='e'

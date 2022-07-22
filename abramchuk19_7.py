import time


def timer(method):
    def timing(*args, **kw):
        ts = time.time()
        result = method(*args, **kw)
        te = time.time()
        delta = (te - ts) * 1000
        print(f'{method.__name__} виконувався {delta:2.2f} ms')
        return result

    return timing


def timeit_all_methods(cls):
    class NewCls:
        def __init__(self, *args, **kwargs):
            self._obj = cls(*args, **kwargs)

        def __getattribute__(self, a):
            try:
                x = super().__getattribute__(a)
            except AttributeError:
                pass
            else:
                return x
            attr = self._obj.__getattribute__(a)
            if isinstance(attr, type(self.__init__)):
                return timer(attr)
            else:
                return attr

    return NewCls


@timeit_all_methods
class Fib:

    def fib(self, n):
        if n == 0:
            return 1
        elif n == 1:
            return 1
        else:
            return self.fib(n - 1) + self.fib(n - 2)

    def hello(self):
        print("hello")


print(Fib().fib(35))
Fib().hello()

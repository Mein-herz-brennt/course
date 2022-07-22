# from math import sqrt
# from random import randint
#
#
# def cash(fun):
#     results = {}
#
#     def _cash(*args):
#         if args not in results:
#             results[args] = fun(*args)
#         return results[args]
#
#     return _cash
#
#
# @cash
# def fib(n):
#     if n == 0:
#         return 1
#     elif n == 1:
#         return 1
#     else:
#         return fib(n - 1) + fib(n - 2)
#
#
# @cash
# def is_prime(n):
#     for i in range(2, int(sqrt(n))):
#         if n % i == 0:
#             return False
#         return True
#
#
# def density(a):
#     m = a * 1000
#     passed = 0
#     for _ in range(m):
#         k = randint(1, a)
#         if is_prime(k):
#             passed += 1
#     return passed / m
#
#
# # a = 50
# #
# # print("[1, {}]:{:.0f}%".format(a, 100 * density(a)))
#
#
# def num_liner(fun):
#     def _num(n):
#         print(n + 1)
#         fun(n)
#
#     return _num
# #
#
# @num_liner
# def text_printer(n):
#     with open("789402487", "r", encoding="utf-8") as file:  # замість 789402487 підставиш свій файл
#         k = file.readlines()
#         line = k[n]
#         print(line)
#
#
# def file_reader_by_line(filename):
#     with open(filename, "r", encoding="utf-8") as f:
#         num = len(f.readlines())
#         for i in range(num):
#             text_printer(i)
#
#
# file_reader_by_line("789402487")  # замість 789402487 підставиш свій файл
# from random import randint
#
#
# def matrix_generator(n):  # n - розмірність матриці
#     matrix = []
#     for i in range(n):
#         line = []
#         for j in range(n):
#             line.append(randint(0, 1))
#         matrix.append(line)
#     return matrix
#
#
# def result_generator(n):
#     result = []
#     for i in range(n):
#         line = []
#         for j in range(n):
#             line.append(0)
#         result.append(line)
#     return result
#
#
# def decor(fun):
#     def _matrix(*args):
#         matrix = fun(*args)
#         persent = (len(matrix) * 2) / 100
#         slovar = {}
#         count = 0
#         for i in matrix:
#             for j in i:
#                 if j == 0:
#                     count += 1
#                 else:
#                     slovar[f"цифра{j}"] = j
#         persents = ((len(matrix) * 2) - count) * persent
#         if persents > 0.1:
#             return matrix
#         else:
#             return slovar
#
#     return _matrix
#
#
# @decor
# def sum_matrix(x, y):
#     result = result_generator(len(x))
#
#     for i in range(len(x)):
#
#         for j in range(len(x[0])):
#             result[i][j] = x[i][j] + y[i][j]
#     return result
#
#
# x = matrix_generator(3)
# y = matrix_generator(3)
# c = sum_matrix(x, y)
# print(c)
# from
#
#
# class Point(metaclass= ABCmeta)

# def check_field(cls):
#     return cls
#
#
# class S1mple:
#     _field_types = {"a": bool, "b": int, "c": float, "d": str}
#
#     def __init__(self, a: bool, b: int, c: float, d: str):
#         self.a = a
#         self.b = b
#         self.c = c
#         self.d = d
#
#     def f(self):
#         return "f"
#
#     def g(self):
#         return "g"
#
#
# one_shoot = S1mple(5, 6, 7, 8)
# two_shoot = S1mple(1, 2, 3, 4)
# print(S1mple.__dict__)

"""дз 17_7"""


# from time import clock
#
# clock()
# for i in range(1000):
#     i += 1
# print(clock())
#
#
# #
# import datetime
# import time
#
#
# def timer(method):
#     def timing(*args, **kw):
#         ts = time.time()
#         result = method(*args, **kw)
#         te = time.time()
#         delta = (te - ts) * 1000
#         print(f'{method.__name__} виконувався {delta:2.2f} ms')
#         return result
#
#     return timing
#
#
# def timeit_all_methods(cls):
#     class NewCls:
#         def __init__(self, *args, **kwargs):
#             self._obj = cls(*args, **kwargs)
#
#         def __getattribute__(self, a):
#             try:
#                 x = super().__getattribute__(a)
#             except AttributeError:
#                 pass
#             else:
#                 return x
#             attr = self._obj.__getattribute__(a)
#             if isinstance(attr, type(self.__init__)):
#                 return timer(attr)
#             else:
#                 return attr
#
#     return NewCls
#
#
# @timeit_all_methods
# class Fib:
#
#     def fib(self, n):
#         if n == 0:
#             return 1
#         elif n == 1:
#             return 1
#         else:
#             return self.fib(n - 1) + self.fib(n - 2)
#
#     def hello(self):
#         print("hello")
#
#
# print(Fib().fib(35))
# print(Fib().hello())

# это вспомогательный декоратор будет декорировать каждый метод класса, см. ниже


#
#
# @timeit_all_methods
# class Foo:
#     def a(self):
#         print("метод a начался")
#         time.sleep(0.666)
#         print("метод a кончился")
#
#
# f = Foo()
# f.a()

#
# def cls_decor(cls):
#     class My_class:
#         def __init__(self, *args, **kwargs):
#             self.obj_cls = cls(*args, **kwargs)
#
#         def save(self):
#             with open("saver.txt", "w") as file:
#                 file.write(self.obj_cls.__init__)
#
#         def add_method(self):
#             setattr(self.obj_cls.__init__, self.save(), self.save())
#
#
# class Chill_out():
#     def __init__(self):
#         poh = 0
#
#
#
# import numpy as np
# import matplotlib.pyplot as plt
#
#
# def circle():
#     x1 = np.linspace(1, -1, 1080)
#     x2 = np.linspace(-1, 1, 1080)
#     y1 = np.sqrt(1 - x1 ** 2)
#     y2 = -np.sqrt(1 - x2 ** 2)
#     x = np.hstack((x1, x2))
#     y = np.hstack((y1, y2))
#     return x, y
#
# def poly(n):
#
#
#
# plt.axes(xlim=(-2, 2), ylim=(-1.5, 1.5))
# plt.plot(*circle())
# plt.show()

# from abc import ABCMeta, abstractmethod
#
#
# class Mymeta(metaclass=ABCMeta):
#
#     @abstractmethod
#     def save(self):
#         pass
#     @property
#     def load(self):
#         pass


def decor(*var):
    def onDecorator(cls):
        class onInstance:

            def __init__(self, *args, **kwargs):
                setter = var
                cls.setter = self.flam
                self.wrapped = cls(*args, **kwargs)

            def __getattr__(self, attr):
                return getattr(self.wrapped, attr)

            def __setattr__(self, attr, value):
                if attr == 'wrapped':
                    self.__dict__[attr] = value
                else:
                    setattr(self.wrapped, attr, value)

            def flam(self, *args):
                self.__setattr__('dimension', len(args[0]))
                return onInstance
    return onDecorator

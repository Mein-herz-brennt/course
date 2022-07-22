from math import *


class Numbers_and_matrix:
    def __init__(self, x, k):
        self.x = x
        self.k = k

    def recursion(self):
        xn_list = []
        if self.k < 0:
            print('K < 0')
        else:
            while self.k > 0:
                xp = (self.x ** (2 * self.k)) / factorial(2 * self.k)
                xn = xp
                yield xn
                self.k -= 1


class Product:
    def __init__(self, n):
        self.n = n

    def product(self):
        # element_n = 1 + (1 / (self.n ** 2))
        # n1 = 3 * element_n
        i = 1
        element_n = 1 + (1 / (self.n ** 2))
        n_elements = [element_n]
        while i <= self.n - 1:
            next_element = 1 + (1 / ((self.n - i) ** 2))
            n_elements.append(next_element)
            i += 1

        j = 0
        iteration_list = []

        print(n_elements)
        while j <= len(n_elements) + 2:
            pr = n_elements[j - 1] * n_elements[j]
            j += 1

            p = pr * n_elements[j]
            j += 1

            print(p)

    # def matrix(self):
    #     pass
    #
    # def teylor(self):
    #     pass

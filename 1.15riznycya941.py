# https://www.e-olymp.com/uk/submissions/7350822
import math

n = abs(int(input()))
a = n // 10
b = a // 10
c = a % 10
d = n % 10
print((d * b * c) - (d + b + c))

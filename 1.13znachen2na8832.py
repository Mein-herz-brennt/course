# https://www.e-olymp.com/uk/submissions/7350587
import math

x, y = input().split()
x = float(x)
y = float(y)
c = (x ** 2 - 2 * x * y + 4 * y ** 2) / (x + 5) + (3 * x ** 2 - y ** 2) / (y - 7)
print("%.3f" % c)

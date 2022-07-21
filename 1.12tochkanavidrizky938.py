# https://www.e-olymp.com/uk/submissions/7373802
x, y, n, k, a = [float(d) for d in input().split()]
b = (x + a * n) / (1 + a)
c = (y + a * k) / (1 + a)
print("%.2f" % b, "%.2f" % c)

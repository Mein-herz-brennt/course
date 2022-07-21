#https://www.e-olymp.com/uk/submissions/7548224             90%
from math import log, floor

num = int(input())
factorial = 1
for i in range(num):
    factorial *= (i+1)


print(floor(log(factorial, 10)) + 1)

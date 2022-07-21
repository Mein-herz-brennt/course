"""
https://www.e-olymp.com/uk/submissions/7626743
"""

n = int(input())


def primfacs(n):
    i = 2
    primfac = []
    while i * i <= n:
        while n % i == 0:
            primfac.append(i)
            n = n / i
        i = i + 1
    if n > 1:
        primfac.append(int(n))
    return primfac


print(sorted(primfacs(n)))
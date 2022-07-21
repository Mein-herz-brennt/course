n = int(input())

fib = [1, 0, 1]

i = 3
while fib[i-1] < n:
    fib.append((2 * fib[i-1]) + (3 * fib[i - 3]))
    i += 1
else:
    print(fib[i-2])


# 𝑥0=𝑥2=1, 𝑥1=0, 𝑥𝑛=2𝑥𝑛−1 + 3𝑥𝑛−3,

"""
1, 0, 1, 1+4
"""
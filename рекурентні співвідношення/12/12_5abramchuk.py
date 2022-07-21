n = int(input())

fib = [1, 2]

i = 0

while fib[i] < n:
    fib.append(fib[i] + fib[i + 1])
    i += 1
else:
    print(fib[i-1])



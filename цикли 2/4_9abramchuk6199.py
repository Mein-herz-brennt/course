#https://www.e-olymp.com/uk/submissions/7587644

n = int(input())
values = []

for i in range(n):
    value = int(input())
    values.append(value)

for j in range(n):
    if values[j] % 2:
        print(values[j], 'is odd')
    else:
        print(values[j], 'is even')

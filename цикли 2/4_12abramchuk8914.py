#https://www.e-olymp.com/uk/submissions/7587657

values = []
value = ''

while value != 0:
    value = int(input())
    if value % 2 == 0:
        values.append(value)
else:
    print(sum(values))

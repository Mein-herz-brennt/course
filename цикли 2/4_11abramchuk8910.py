#https://www.e-olymp.com/uk/submissions/7587650

values = []
value = ''

while value != 0:
    value = int(input())
    values.append(value)
else:
    print(sum(values))

#https://www.e-olymp.com/uk/submissions/7587671

herbarij = "GCV"

n = int(input())
values = []

for i in range(n):
    value = int(input())
    values.append(value)

for i in range(len(values)):
    k = int(values[i])
    while k != 0:
        herbarij = herbarij[2] + herbarij[0] + herbarij[1]
        k = k - 1
    else:
        print(herbarij)
        herbarij = "GCV"

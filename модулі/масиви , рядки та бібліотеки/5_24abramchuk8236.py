"""
https://www.e-olymp.com/uk/submissions/7626951
"""

n = int(input())
array = list(input().split())
array = list(map(int, array))

array_par = []
array_nopar = []

for i in range(n):
    if array[i] % 2 == 0:
        array_par.append(array[i])
    else:
        array_nopar.append(array[i])

result = sorted(array_nopar)
result += sorted(array_par, reverse=True)

string = ''

for j in range(len(result)):
    string += str(result[j]) + ' '

print(string)
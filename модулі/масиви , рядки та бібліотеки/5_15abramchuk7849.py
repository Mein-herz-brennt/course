"""
https://www.e-olymp.com/uk/submissions/7626792
"""

n = int(input())
array = list(input().split())

array = list(map(int, array))
minimum = min(array)
maximum = max(array)
max_index = []
min_index = []

for i in range(n):
    if array[i] == minimum:
        min_index.append(i)
    elif array[i] == maximum:
        max_index.append(i)

for j in range(n):
    if j in max_index:
        array[j] = minimum
    elif j in min_index:
        array[j] = maximum

string = ''
for x in range(n):
    string += str(array[x]) + ' '

print(string)
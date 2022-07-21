"""
https://www.e-olymp.com/uk/submissions/7626665
"""

n = int(input())
array_one = list(input().split())
result = []
for i in range(n):
    if array_one[i] not in result:
        result.append(array_one[i])

string = ''

for j in range(len(result)):
    string += result[j] + ' '

print(string)
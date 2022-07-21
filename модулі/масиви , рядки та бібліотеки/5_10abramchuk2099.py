"""
https://www.e-olymp.com/uk/submissions/7626638
"""

n = int(input())
array_one = list(input().split())
m = int(input())
array_two = list(input().split())

result = []

for i in range(n):
    if array_one[i] not in array_two:
        result.append(array_one[i])

string = str(len(result)) + '\n'

for j in range(len(result)):
    string += result[j] + ' '

print(string)
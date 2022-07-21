#https://www.e-olymp.com/uk/submissions/7690537
string = input()
n = int(input())
result = ''
upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

for i in range(len(string)):
    k = n
    index = upper.find(string[i])
    if index - k < 0:
        k = len(upper) - k + index
        result += upper[k]
    else:
        result += upper[index - k]

print(result)
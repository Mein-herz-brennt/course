#https://www.e-olymp.com/uk/submissions/7927866

def transpose(matr):
    res = []
    n = len(matr)
    m = len(matr[0])
    for j in range(m):
        tmp = []
        for i in range(n):
            tmp = tmp + [matr[i][j]]
        res = res + [tmp]
    return res


num = input()
n = int(input())
array = []
for i in range(n):
    sub_n = list(input().split())
    array.append(sub_n)

array = transpose(array)

for i in array:
    if num in i:
        print("YES")
    else:
        print("NO")

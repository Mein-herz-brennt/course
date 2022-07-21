#https://www.e-olymp.com/uk/submissions/7927873
def ret(matr):
    res = []
    n = len(matr)
    m = len(matr[0])
    for j in range(m):
        tmp = []
        for i in range(n):
            tmp = tmp + [matr[i][j]]
        res = res + [tmp]
    return res


n, m = list(input().split())
array = []
string = ''

for i in range(int(n)):
    sub_n = list(map(int, list(input().split())))
    array.append(sub_n)


res = ret(array)

new_res = list(map(list,map(reversed, res)))

for i in range(int(m)):
    for j in range(int(n)):
        string += str(new_res[i][j]) + ' '
    string += "\n"
print(m,n)
print(string)
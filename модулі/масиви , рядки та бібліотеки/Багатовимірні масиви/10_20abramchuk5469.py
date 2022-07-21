# https://www.e-olymp.com/uk/submissions/7927883 77%

n = int(input())
array = []
for i in range(n):
    sub_n = list(map(float, list(input().split())))
    array.append(sub_n)


def eliminate(r1, r2, col, target=0):
    fac = (r2[col] - target) / r1[col]
    for i in range(len(r2)):
        r2[i] -= fac * r1[i]


def gauss(a):
    for i in range(len(a)):
        if a[i][i] == 0:
            for j in range(i + 1, len(a)):
                if a[i][j] != 0:
                    a[i], a[j] = a[j], a[i]
                    break
            else:
                print("NO")
                return -1
        for j in range(i + 1, len(a)):
            eliminate(a[i], a[j], i)
    for i in range(len(a) - 1, -1, -1):
        for j in range(i - 1, -1, -1):
            eliminate(a[i], a[j], i)
    for i in range(len(a)):
        eliminate(a[i], a[i], i, target=1)
    return a


def inverse(a):
    tmp = [[] for _ in a]
    for i, row in enumerate(a):
        assert len(row) == len(a)
        tmp[i].extend(row + [0] * i + [1] + [0] * (len(a) - i - 1))
    gauss(tmp)
    ret = []
    for i in range(len(tmp)):
        ret.append(tmp[i][len(tmp[i]) // 2:])
    return ret


inv_array = inverse(array)
print("YES")
string = ""
for i in inv_array:
    for j in range(len(i)):
        string += str(i[j]) + ' '
    string += ("\n")

print(string)
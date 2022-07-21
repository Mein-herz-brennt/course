n = int(input())
x = [1, 1, 1]


def pad(n):
    x = [1, 1, 1]
    # x[3] = x[1] + x[0]
    # x.append(x[3])
    j = 2

    for i in range(0, n - 1):
        x[0] = x[1] = x[2] = 1
        j += 1
        print(j)
        x[i] = x[len(x) - 2] + x[len(x) - 3]
        print(x[i])

        x.append(x[i])
        if x[i] > n:
            return j


print(pad(n))

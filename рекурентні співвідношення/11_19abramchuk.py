n = int(input())
z = int(input())


def nat(a):
    nat_list = []
    i = 1
    for i in range(10 ** 2 + 1):
        nat_list.append(str(i))
    return "".join(nat_list)[a]


def ten(a):
    ten_list = []
    for i in range(a):
        ten_list.append(str(10 ** i))
    return "".join(ten_list)[a]


def kv(a):
    kv_list = []
    for i in range(10 ** 2 + 1):
        kv_list.append(str(i ** 2))
    return "".join(kv_list)[a]


def fib(a):
    for i in range(10):
        if n in (1, 2):
            return 1
    return (n - 1) + (n - 2)
    fib_list = []
    i = 1
    fib_list.append(str(i))
    return "".join(fib_list)[a]


if z == 0:
    print(ten(n))
elif z == 1:
    print(nat(n))
elif z == 2:
    print(kv(n))
elif z == 3:
    print(fib(n))

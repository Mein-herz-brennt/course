#https://www.e-olymp.com/uk/submissions/7755213 30%
def convert_base(num, to_base=2, from_base=10):
    if isinstance(num, str):
        n = int(num, from_base)
    else:
        n = int(num)
    alphabet = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    if n < to_base:
        return alphabet[n]
    else:
        return convert_base(n // to_base, to_base) + alphabet[n % to_base]


def range_prod(lo, hi):
    if lo + 1 < hi:
        mid = (hi + lo) // 2
        return range_prod(lo, mid) * range_prod(mid + 1, hi)
    if lo == hi:
        return lo
    return lo * hi


def treefactorial(n):
    if n < 2:
        return 1
    return range_prod(1, n)


n, k = list(input().split())

if k == '10':
    factorial = treefactorial(int(n))
else:
    factorial = convert_base(to_base=int(k), num=treefactorial(int(n)))
print(len(str(factorial)) - len(str(int(str(factorial)[::-1]))))

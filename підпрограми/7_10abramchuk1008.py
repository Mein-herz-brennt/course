# https://www.e-olymp.com/uk/submissions/7755191 89%
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


base = list(input().split())

number = input()

print(convert_base(number, int(base[1]), int(base[0])))

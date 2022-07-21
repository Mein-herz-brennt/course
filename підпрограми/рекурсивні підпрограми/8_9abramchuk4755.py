# https://www.e-olymp.com/uk/submissions/7762783
def convert_base(num):
    to_base = 13
    n = int(num)
    alphabet = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    if n < to_base:
        return alphabet[n]
    else:
        return convert_base(n // to_base) + alphabet[n % to_base]


number = input()

print(convert_base(number))

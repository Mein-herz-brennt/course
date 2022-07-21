# https://www.e-olymp.com/uk/submissions/7548152
number = int(input())
out_number = ''
"привіт світ"

for i in range(len(str(number))):
    num = int(str(number)[i])
    if num % 2 == 0:
        out_number += str(num + 1)
    else:
        out_number += str(num - 1)
print(int(out_number))


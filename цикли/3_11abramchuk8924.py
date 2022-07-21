# https://www.e-olymp.com/uk/submissions/7548192
number = int(input())
out_number = 0
buffer = 0

for i in range(len(str(number))):
    num = int(str(number)[i])
    if num % 2 == 0:
        out_number += num

if out_number != 0:
    print(out_number)
elif '0' in str(number):
    print(0)
else:
    print(-1)

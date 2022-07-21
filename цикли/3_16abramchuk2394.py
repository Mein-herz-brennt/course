# https://www.e-olymp.com/uk/submissions/7548291     60%

m = int(input())
str_m = str(m)
while not str(m**2).endswith(str(m)):
    m -= 1
else:
    print(m)

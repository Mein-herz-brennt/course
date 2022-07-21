#https://www.e-olymp.com/uk/submissions/7448244
a = int(input())
if a % 4 != 0 or a % 400 != 0 and a % 100 == 0:
    print("NO")
else:
    print("YES")
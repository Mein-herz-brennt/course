#https://www.e-olymp.com/uk/submissions/7440695
a ,b ,c = [int(d) for d in input().split()]
if a==b==c :
    print(1)
elif a==b!=c or a==c!=b or b==c!=a :
    print(2)
elif a!=b!=c :
    print(3)
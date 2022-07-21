k = int(input())

x = str(x)
if k  == 1 :
    p =  "".join(str(-1*x))
    print(p)
elif k // 2 == 0 :
    xk = ((1**k)*(x**k))/k
    print(str(xk))
else:
    xk = (((-1)**k)*(x**k))/k
    print(str(xk))
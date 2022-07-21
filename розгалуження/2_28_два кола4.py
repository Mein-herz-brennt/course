#https://www.e-olymp.com/uk/submissions/7448119
x1 ,y1 ,r1 ,x2 ,y2 ,r2 = [float(d) for d in input().split()]
if( x1 == x2 and y1 == y2 and r1 == r2 ):
    print(-1)

elif (( (x2-x1)*(x2-x1) + (y2-y1)*(y2-y1) )**(1/2)) == r1+r2 or (( (x2-x1)*(x2-x1) + (y2-y1)*(y2-y1) )**(1/2)) + r2 == r1 or (( (x2-x1)*(x2-x1) + (y2-y1)*(y2-y1) )**(1/2)) + r1 == r2:
    print(1)
elif ( (x2-x1)*(x2-x1) + (y2-y1)*(y2-y1) )**(1/2) > r1+r2  :
    print(0)
elif ( ( (x2-x1)*(x2-x1) + (y2-y1)*(y2-y1) )**(1/2) ) + r2 < r1 or (( (x2-x1)*(x2-x1) + (y2-y1)*(y2-y1) )**(1/2)) +r1 < r2:
    print(0)
elif (( (x2-x1)*(x2-x1) + (y2-y1)*(y2-y1) )**(1/2) < (r1+r2)):
    print(2)
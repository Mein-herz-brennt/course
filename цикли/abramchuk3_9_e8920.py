#https://www.e-olymp.com/uk/submissions/7535577
n=int(input())
a=0
c=1
while a<n:
    if c%2 and c%3 and c%5:
        print(c, end=" ")
        a += 1
    c += 1


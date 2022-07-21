#https://www.e-olymp.com/uk/submissions/7927845

n = int(input())
array = []
for i in range(n):
    sub_n = list(map(int, list(input().split())))
    array.append(sub_n)


sum_one = 0
sum_two = 0

for i in range(n):
    for j in range(n):
        if j == n-i-1:
            sum_two += array[i][j]
        elif j == i:
            sum_one += array[i][j]

if n % 2 != 0:
    sum_one += array[n//2][n//2]
print(sum_one, sum_two)
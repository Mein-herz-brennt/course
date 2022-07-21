#https://www.e-olymp.com/uk/submissions/7587636

n = int(input())

count = 1
result = ''

while count ** 3 < n:
    result += (str(count**3) + ' ')
    count = count + 1
else:
    print(result)

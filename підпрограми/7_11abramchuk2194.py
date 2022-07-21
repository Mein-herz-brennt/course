



def palindrom(string):
    if string == string[::-1]:
        return True
    else:
        return False

j = 0
for i in range(20000, 105000):
    if palindrom(i):
        j += 1
print(j)



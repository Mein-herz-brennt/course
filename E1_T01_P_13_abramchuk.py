j = 0

for i in range(20000,105000):
  string = str(i)
  if string == string[::-1]:
    pal_list = "".join(string)
    j += 1

print(j)
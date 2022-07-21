#https://www.e-olymp.com/uk/submissions/7762814             використовує файли для читання і запису!
def run(f):
    t = (f + 1) // 2
    if f == 0:
        return 0
    else:
        return t * t + run((f // 2))


list_nums = []

f = open('input.txt')
line = f.readline()
while line:
    list_nums.append(int(line))
    line = f.readline()
f.close()

output = ''
for i in list_nums:
    output += str(run(i)) + '\n'

with open("output.txt", "w") as file:
    file.write(output)

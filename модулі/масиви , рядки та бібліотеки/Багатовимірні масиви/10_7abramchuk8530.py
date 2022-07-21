#https://www.e-olymp.com/uk/submissions/7927833

lines = int(input())
array = []
for i in range(lines):
    sub_line = list(input().split())
    array.append(sub_line)
else:
    size = list(map(int, list(input().split())))

new_str_array = ''

for i in range(size[0]):
    for j in range(size[1]):
        new_str_array += array[i][j] + " "
    new_str_array += "\n"

print(new_str_array)
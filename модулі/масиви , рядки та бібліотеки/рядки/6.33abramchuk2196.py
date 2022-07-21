

#https://www.e-olymp.com/uk/submissions/7690592

string = input()
n = int(input())
attributes = []

for i in range(n):
    attributes.append(list(input().split()))


def sub_strings(string: str, i: int, j: int) -> str:
    substring = ''
    for x in range(j - i):
        substring += string[x + i]
    return substring


for i in attributes:
    if i[0] == "S":
        string = string[:int(i[1])-1] + ''.join(sorted(sub_strings(string, int(i[1]) - 1, int(i[2])))) +\
                 string[int(i[2]):]
    if i[0] == "R":
        string = string[:int(i[1])-1] + sub_strings(string, int(i[1]) - 1, int(i[2]))[::-1] + string[int(i[2]):]

print(string)
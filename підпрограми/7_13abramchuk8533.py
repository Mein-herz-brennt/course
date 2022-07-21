# https://www.e-olymp.com/uk/submissions/7755204

def unmached(string):
    string_two = ''
    for i in range(4):
        if string[i] in string_two:
            return False
        else:
            string_two += string[i]
    else:
        return True


num1, num2 = list(input().split())
num_list = []
for i in range(int(num1), int(num2) + 1):
    if unmached(str(i)):
        num_list.append(str(i))

print(" ".join(num_list))

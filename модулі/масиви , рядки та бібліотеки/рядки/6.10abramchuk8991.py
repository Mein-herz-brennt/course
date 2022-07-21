#https://www.e-olymp.com/uk/submissions/7690515   6.10
alphabet = 'qwertyuiopasdfghjklzxcvbnm'

string = input()
result = ''

for i in range(len(string)):
    if string[i] in alphabet:
        result += string[i] * 2
    else:
        result += string[i]

print(result)

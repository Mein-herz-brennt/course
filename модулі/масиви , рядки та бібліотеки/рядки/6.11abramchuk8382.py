"""
https://www.e-olymp.com/uk/submissions/7690552
86%  НЕ ПРОХОДИТЬ 2 ТЕСТИ!
"""


password = input()

result = 0

symbols = '!"#$%&‘()*+'
upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
lower = 'abcdefghijklmnopqrstuvwxyz'
nums = '1234567890'

if ' ' in password:
    password = password.replace(' ', '')

for i in range(len(password)):
    if password[i] in lower:
        result += 1
        break

for i in range(len(password)):
    if password[i] in upper:
        result += 1
        break

for i in range(len(password)):
    if password[i] in nums:
        result += 1
        break

for i in range(len(password)):
    if password[i] in symbols:
        result += 1
        break

if len(password) > 7:
    result += 1

print(result)
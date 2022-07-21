#https://www.e-olymp.com/uk/submissions/7855042  90%
import re

with open("input.txt", "r") as file:
    text = file.read()

text = re.sub('[^A-Za-z]', ' ', text)

text = sorted(list(set(list(text.lower().split()))))

s = ""

for i in text:
    s += i + "\n"

with open("output.txt", "w") as file:
    file.write(s)
from random import randint
import re


def privet_fail(n):
    list_slov = []
    for i in range(n):
        slovo = ""
        num1 = randint(0, 3)
        num2 = randint(0, 9)
        slovo += str(num1)
        slovo += str(num2)
        slovo += "."
        num3 = randint(0, 1)
        num4 = randint(0, 9)
        slovo += str(num3)
        slovo += str(num4)
        slovo += "."
        num5 = randint(0, 2)
        num6 = randint(0, 9)
        num7 = randint(0, 9)
        num8 = randint(0, 9)
        slovo += str(num5)
        slovo += str(num6)
        slovo += str(num7)
        slovo += str(num8)
        slovo += "\n"
        list_slov.append(slovo)
    return list_slov


with open("dates.txt", "w") as file:
    file.writelines(privet_fail(10000))

with open("dates.txt", "r") as file:
    text = file.readlines()
    text = list(text)
    for i in range(1000):
        num = randint(0, 9999)
        text[num] = "__.__.____\n"

with open("dates.txt", "w") as file:
    file.writelines(text)

with open("dates.txt", "r") as file:
    textik = file.read()


def zamena_regular(text, date):
    finder = re.compile(r"\d{2}\.\d{2}\.\d{4}\n")
    finder_low = re.compile(r"_{2}\._{2}\._{4}")
    raw_text = re.findall(finder, text)
    raw_low = re.findall(finder_low, text)

    with open("dates.txt") as f:
        length_text = f.readlines()
        length = len(length_text)

    for i in range(length):
        if length_text[i] == "__.__.____\n":
            length_text[i] = date

    print(f"кількість пропусків: {len(raw_low)}")
    print(f"кількість дат: {len(raw_text)}")

    with open("dates.txt", "w") as files:
        files.writelines(length_text)


zamena_regular(textik, "29.11.2021\n")

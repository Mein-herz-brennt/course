import re


def anti_hol(s):
    result = []
    txt = s.split()
    for i in txt:
        if len(i) <= 2:
            result.append(i)
        else:
            result.append(re.sub(r'[AEIOUY]', '', i, flags=re.IGNORECASE))
    return result


with open("text.txt", "r") as file:
    text = file.read()

with open("new_text.txt", "w") as f:
    f.write(" ".join(anti_hol(text)))

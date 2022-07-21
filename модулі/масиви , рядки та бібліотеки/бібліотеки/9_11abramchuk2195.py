#https://www.e-olymp.com/uk/submissions/7855033 87%
import re
ls = list(input().split())
vocab = []
text = ""
for i in range(int(ls[0])):
    vocab.append(input())
else:
    for i in range(int(ls[1])):
        text += input()
        text += " "

vocab = set(vocab)
text = re.sub('[^A-Za-z]', ' ', text)
text = text.lower()

words = set(list(text.split()))

if len(words - vocab) == 0 and len(vocab-words) == 0:
    print("Everything is going to be OK.")
elif not len(words - vocab) == 0 and len(vocab-words) == 0:
    print("Some words from the text are unknown.")
elif len(words - vocab) == 0 and not len(vocab-words) == 0:
    print("The usage of the vocabulary is not perfect.")
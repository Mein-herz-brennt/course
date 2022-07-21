#https://www.e-olymp.com/uk/submissions/7855027
word1 = set(list(input()))
word2 = set(list(input()))

if len(list(word2 - word1)) == 0:
    print("Ok")
else:
    print("No")
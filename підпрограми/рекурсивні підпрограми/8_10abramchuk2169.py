#https://www.e-olymp.com/uk/submissions/7762802
def permutations(head, tail=''):
    if len(head) == 0:
        print(tail)
    else:
        for i in range(len(head)):
            permutations(head[0:i] + head[i + 1:], tail + head[i] + ' ')


n = int(input())
comb = ''

for i in range(n):
    comb += str(i+1)

permutations(comb)

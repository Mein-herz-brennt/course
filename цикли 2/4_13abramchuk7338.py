#https://www.e-olymp.com/uk/submissions/7587668


def num_sum(number):
    string = str(number)
    result = 0
    for j in range(len(string)):
        result += int(string[j])
    else:
        return result


n = int(input())
result = 0

for i in range(10, 100):
    if num_sum(i) == num_sum(i*n):
        result += 1
else:
    print(result)

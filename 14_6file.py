arry = [1, 2, 3, 3, 1, 3, 4, 5, 6]

k = [1, 4, 5, 5, 5, 6, 77, 7, 7, 8, 8, 9, 9, 9, 8, 8, 8]



def enumerin(array):
    j = 0
    for i in array:
        i += 1
        j += 1
    return j


def sumix(array):
    for i in array:
        suma_2first = array[0] + array[i + 1]
        suma = suma_2first + array[i + 1]
        i += 1
    return suma

for i in
print(enumerin(k), sumix(arry))

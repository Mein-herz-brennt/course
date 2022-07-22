import numpy as np

test = 1000

array = np.random.randint(1, 10, 2 * test)
array.shape = (test, 2)

ln = []
for i in range(len(array) - 1):
    lnghts = np.sqrt((array[i + 1][0] - array[i + 1][0]) ** 2 + (array[i + 1][1] - array[i][1]) ** 2)
    ln.append(lnghts)


def triangle(ln):
    ln.sort()
    ln = np.array(ln).reshape(333, 3)

    for i in range(len(ln)):
        if ln[i][0] != ln[i][1]:
            np.delete(ln, i)
        elif ln[i][1] != ln[i][2]:
            np.delete(ln, i)
        elif ln[i][0] != ln[i][2]:
            np.delete(ln, i)

    return len(ln)

print(f"кількість рівносторонніх трикутників {triangle(ln)}")
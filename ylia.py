import numpy as np
import matplotlib.pyplot as plt

# нол не беремо бо на нього нельзя ділить
n = np.arange(1, 100)


@np.vectorize
def lim(x):
    return (np.sqrt(x * ((x ** 4) - 1) - np.sqrt((x ** 3) - 1) * ((x ** 2) + 2))) / np.sqrt(x)


plt.plot(n, lim(n), "r")
plt.hlines(2, 1, 10, colors="g", linestyles="--")
print(lim(n))
print("Ліміт = 10")
plt.show()

import numpy as np
import matplotlib.pyplot as plt

an = np.arange(1, 10000)


def lim(n):
    return (((n - 1) ** 4) - (n + 2) ** 4) / (((2 * n) + 1) ** 3) + (n - 1) ** 3


plt.hlines(0, 1, 2, colors="r", linestyles="--")
plt.plot(an, lim(an))

plt.show()

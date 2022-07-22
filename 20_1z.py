import numpy as np
import matplotlib.pyplot as plt


an = np.arange(1, 10000)


@np.vectorize
def lim(n):
    return (1 + (1/n))**n


print(lim(an))


plt.plot(an, lim(an), "b")
plt.vlines(0, 2, 2.7, colors="r", linestyles="--")
plt.show()

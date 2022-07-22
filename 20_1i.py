import numpy as np
import matplotlib.pyplot as plt

an = np.arange(0, 10)


@np.vectorize
def lim(n):
    return ((5*n**2 + 7*n + 1)/(5*n**2 + 3*n + 6))**(n-3)


print(lim(an))

# збіжний до 2.225

plt.hlines(0, 1, 2.225, colors="r", linestyles="--")
plt.plot(an, lim(an))
plt.show()
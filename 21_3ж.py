import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation

a = -10
b = 10

x = np.linspace(a, b, int(b - a) * 100)

fig = plt.figure()
plt.axis([a, b, -(b - a)*10, (b-a)*10])
plt.plot(x, 1/(1+x))
line, = plt.plot([], [], "--r")


def taylor(n, k):
    s = n.copy()
    nk = n.copy()
    for i in range(k):
        nk = ((-1)**i)*(n**i)
        s += nk
    return s


def anime(i):
    y = taylor(x, i+1)
    line.set_data(x, y)


anim = FuncAnimation(
    fig,
    anime,
    frames=10,
    interval=1000,
    repeat=True
)

plt.show()

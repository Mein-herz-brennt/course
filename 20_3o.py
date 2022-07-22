import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation

a = -np.pi / 2
b = np.pi / 2

x = np.linspace(a, b, int(b - a) * 100)

fig = plt.figure()
plt.axis([a, b, -(b - a)*3/8, (b-a)*3/8])
plt.plot(x, np.arcsin(x))
line, = plt.plot([], [], "--r")


def arc_sin_taylor(n, k):
    s = n.copy()
    nk = n.copy()
    for i in range(1, k):
        nk = ((2 * i - 1) * (n ** (2 * i + 1))) / ((2 * i) * (2 * i + 1))
        s += nk
    return s


def anime(i):
    y = arc_sin_taylor(x, i+1)
    line.set_data(x, y)


anim = FuncAnimation(
    fig,
    anime,
    frames=50,
    interval=5,
    repeat=True
)
anim.save("20_3o.gif", writer="pillow")
plt.show()

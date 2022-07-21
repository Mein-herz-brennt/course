from flower import Flower
from random import randint

for i in range(51):
    h = randint(100, 200)
    l = randint(40, 60)
    r = randint(20, 30)
    x = randint(-200, 100)

    Flower(h, l, r, x).flower()

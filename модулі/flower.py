from turtle import *


class Flower:
    def __init__(self, height, lenght, radius, ox):
        self.h = height
        self.l = lenght
        self.r = radius
        self.x = ox


    def flower(self):
        hideturtle()
        speed(0)
        width(5)

        color('green')

        up()
        goto(self.x, -100)
        down()
        goto(self.x, self.h)
        up()

        goto(self.x, self.h / 10)
        down()
        circle(self.l, 70)
        up()
        goto(self.x, self.h / 10)
        down()
        circle(-self.l, 70)
        up()
        goto(self.x, self.h / 2)
        down()
        circle(self.l, -70)
        up()
        goto(self.x, self.h / 2)
        down()
        circle(-self.l, -70)
        up()

        color('yellow', 'orange')
        begin_fill()

        goto(self.x, self.h)
        down()
        circle(self.r)
        right(90)
        end_fill()
        
        color("blue")


        for i in range(9):
            circle(self.r, 260)
            left(180)
        
        up()

Flower(100, 50, 30, 20).flower()
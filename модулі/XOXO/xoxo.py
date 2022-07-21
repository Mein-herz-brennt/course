from turtle import *

#1  2  3
#4  5  6   => номери полів (погано розібрався з визначенням позиції курсора)
#7  8  9

class Tic_tac_toe:
    def __init__(self, k):
        self.k = k

    def board(self):
        screensize(1000, 1000)
        width(5)
        up()
        goto(125, 450)
        down()
        goto(125, -450)
        up()
        goto(-125, 450)
        down()
        goto(-125, -450)
        up()
        goto(-450, -125)
        down()
        goto(450, -125)
        up()
        goto(450, 125)
        down()
        goto(-450, 125)
        up()

    def zero(self):
        up()
        if self.k == 1:
            color('green')
            goto(-250, 300)
            down()
            circle(-75)
            up()
        elif self.k == 2:
            color('green')
            goto(0, 300)
            down()
            circle(-75)
            up()
        elif self.k == 3:
            color('green')
            goto(250, 300)
            down()
            circle(-75)
            up()
        elif self.k == 4:
            color('green')
            goto(-250, 75)
            down()
            circle(-75)
            up()
        elif self.k == 5:
            color('green')
            goto(0, 75)
            down()
            circle(-75)
            up()
        elif self.k == 6:
            color('green')
            goto(-250, 75)
            down()
            circle(-75)
            up()
        elif self.k == 7:
            color('green')
            goto(-250, -150)
            down()
            circle(-75)
            up()
        elif self.k == 8:
            color('green')
            goto(0, -150)
            down()
            circle(-75)
            up()
        elif self.k == 9:
            color('green')
            goto(250, -150)
            down()
            circle(-75)
            up()

    def cross(self):
        up()
        color('red')

        if self.k == 1:
            goto(-300, 300)
            down()
            goto(-200, 200)
            up()
            goto(-300, 200)
            down()
            goto(-200, 300)
            up()
        elif self.k == 2:
            goto(50, 300)
            down()
            goto(-50, 200)
            up()
            goto(50, 200)
            down()
            goto(-50, 300)
            up()
        elif self.k == 3:
            goto(300, 300)
            down()
            goto(200, 200)
            up()
            goto(300, 200)
            down()
            goto(200, 300)
            up()
        elif self.k == 4:
            goto(-300, 75)
            down()
            goto(-200, -75)
            up()
            goto(-300, -75)
            down()
            goto(-200, 75)
            up()
        elif self.k == 5:
            goto(50, 75)
            down()
            goto(-50, -75)
            up()
            goto(50, -75)
            down()
            goto(-50, 75)
            up()
        elif self.k == 6:
            goto(300, 75)
            down()
            goto(200, -75)
            up()
            goto(300, -75)
            down()
            goto(200, 75)
            up()
        elif self.k == 7:
            goto(-300, -300)
            down()
            goto(-200, -200)
            up()
            goto(-300, -200)
            down()
            goto(-200, -300)
            up()
        elif self.k == 8:
            goto(-50, -300)
            down()
            goto(50, -200)
            up()
            goto(-50, -200)
            down()
            goto(50, -300)
            up()
        elif self.k == 9:
            goto(-50, -300)
            down()
            goto(50, -200)
            up()
            goto(-50, -200)
            down()
            goto(50, -300)
            up()

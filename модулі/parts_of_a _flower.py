from time import *

class Petal:
	def __init__(self, lenght):
		self.l = lenght

	def petal(self):
	  for i in range(9):
	    circle(r, 260)
	    left(180)

class Inflorescences:
	def __init__(self, height, radius):
		self.h = height
		self.r = radius

	def _inflorescences(self):
      goto(0, self.h)
      down()
      circle(self.r)
      right(90)

      for i in range(9):
        circle(self.r, 260)
        left(180)
      up()



class Leaf:
	def __init__(self, lenght, hight):
		self.l = lenght
		self.h = hight

    def leaf(self):
      goto(0, self.h / 10)
      down()
      circle(self.l, 70)
      up()
      goto(0, self.h / 10)
      down()
      circle(-self.l, 70)
      up()
      goto(0, self.h / 2)
      down()
      circle(self.l, -70)
      up()
      goto(0, self.h / 2)
      down()
      circle(-self.l, -70)
      up()

class Stem:
	def __init__(self, height):
		self.h = height

	def stem(self):
	up()
	goto(0, -100)
	down()
	goto(0, self.h)
	up()

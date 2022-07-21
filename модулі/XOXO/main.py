from xoxo import *

#1  2  3
#4  5  6   => номери полів
#7  8  9

hideturtle()
speed(0)
Tic_tac_toe(0).board()

for i in range(6):
    cros = int(input('введіть номер квадрату для хрестика: '))
    Tic_tac_toe(cros).cross()
    zeros = int(input('введіть номер квадрату для нулика: '))
    Tic_tac_toe(zeros).zero()


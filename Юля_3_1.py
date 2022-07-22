from math import sqrt

# [lenght, width, higdt, type] or [lenght, width,type] type = 'тип основиб буває : triangle, square "фігура що має
# чотири попарно паралельні та рівні сторони", circle "коло"' , для трикутника в списку вказуємо довжини всіх сторін
# для кола - радіус ну і для трьохвимірних звісно висоту
# prizma = призма culindr = циліндр kylia = куля

class Figure:
    def __init__(self, figure):
        self.figure = figure
        self.len = len(figure)

    def dimention(self):
        if self.figure[self.len-1] == 'triangle' or 'square' or 'circle':
            return 'Фігура 2-вимірна'
        else:
            return 'Фігура 3-вимірна'

    def perimetr(self):
        if self.figure[self.len - 1] == 'triangle':
            per = self.figure[0]+self.figure[1]+self.figure[2]
            return per
        elif self.figure[self.len - 1] == 'square':
            per = 2 * (self.figure[0] + self.figure[1])
            return per
        elif self.figure[self.len - 1] == 'circle':
            per = 2 * self.figure[0]
            return f"{per}pi"
        else:
            return None

    def square(self):
        if self.figure[self.len - 1] == 'triangle':
            p = (self.figure[0]+self.figure[1]+self.figure[2])/2
            s = sqrt(p * (p - self.figure[0]) * (p - self.figure[1]) * (p - self.figure[2]))
            return s
        elif self.figure[self.len - 1] == 'square':
            s = self.figure[0] * self.figure[1]
            return s
        elif self.figure[self.len - 1] == 'circle':
            s = self.figure[0] ** 2
            return f"{s}pi"
        else:
            return None

    def square_surface(self):
        if self.figure[self.len - 1] == 'prizma':
            p = 2 * (self.figure[0] + self.figure[1])
            sb = p * self.figure[2]
            return sb
        elif self.figure[self.len - 1] == 'prizma_triangle':
            p = self.figure[0] + self.figure[1] + self.figure[2]
            sb = p * self.figure[4]
            return sb
        elif self.figure[self.len - 1] == 'culindr':
            p = self.figure[0] * 2
            sb = p * self.figure[1]
            return f"{sb}pi"
        elif self.figure[self.len - 1] == 'kylia':
            sb = 4 * (self.figure[0] ** 2)
            return sb
        else:
            return None

    def height(self):
        if self.figure[self.len - 1] == 'triangle' or 'square' or 'circle':
            return None
        elif self.figure[self.len - 1] == 'prizma':
            return self.figure[2]
        elif self.figure[self.len - 1] == 'prizma_triangle':
            return self.figure[4]
        elif self.figure[self.len - 1] == 'kylia':
            return self.figure[0] * 2  # діаметр є висотою кулі
        elif self.figure[self.len - 1] == 'culindr':
            return self.figure[2]

    def volume(self):
        if self.figure[self.len - 1] == 'triangle':
            p = (self.figure[0]+self.figure[1]+self.figure[2])/2
            s = sqrt(p * (p - self.figure[0]) * (p - self.figure[1]) * (p - self.figure[2]))
            return s
        elif self.figure[self.len - 1] == 'square':
            s = self.figure[0] * self.figure[1]
            return s
        elif self.figure[self.len - 1] == 'circle':
            s = self.figure[0] ** 2
            return f"{s}pi"
        elif self.figure[self.len - 1] == 'prizma':
            v = self.figure[0]*self.figure[1]*self.figure[2]
            return v
        elif self.figure[self.len - 1] == 'prizma_triangle':
            return "Треба формула"
        elif self.figure[self.len - 1] == 'kylia':
            v = (4/3) * (self.figure[0]**3)
            return f"{v}pi"
        elif self.figure[self.len - 1] == 'culindr':
            v = (self.figure[0] ** 2) * self.figure[1]
            return v

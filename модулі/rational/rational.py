class RationalEror(ZeroDivisionError):
    def __init__(self, numer, den):
        self.den = den
        self.numer = numer
        if self.den == 0:
            e = ZeroDivisionError('Деление на ноль')
            raise e
        else:
            pass

    def ret1(self):
        return self.numer
    def ret2(self):
        return self.den    



class Rational:
    def __init__(self, numerator, denominator):
        numr = RationalEror(numerator, denominator).ret1()
        denom = RationalEror(numerator, denominator).ret2()

        for i in list([11, 10, 9, 8, 7, 6, 5, 4, 3, 2]):

            if numerator % i == 0 and denominator % i == 0:
                self.n = numr / i
                self.d = denom / i
            else:
                self.n = numr
                self.d = denom
        

    def __str__(self):
        return '{}/{}'.format(self.n, self.d)

    def __add__(self, other):
        if other.d == 0:
            other.d = 1
        else:
            pass
        if other.d == self.d:
            k = self.n + other.n
            return '{}/{}'.format(k, self.d)
        else:
            new = (self.n * other.d) + (other.n * self.d)
            now = self.d * other.d
            return '{}/{}'.format(new, now)

    def __sub__(self, other):
        if other.d == 0:
            other.d = 1
        else:
            pass
        if other.d == self.d:
            k = self.n - other.n
            return '{k}/{self.d}'
        else:
            new = ((self.n * other.d) - (other.n * self.d))
            now = self.d * other.d
            return '{}/{}'.format(new, now)

    def __mul__(self, other):
        if other.d == 0:
            other.d = 1
        else:
            pass
        star = self.n * other.n
        newstar = self.d * other.d
        return '{}/{}'.format(star, newstar)

    def __truediv__(self, other):
        if other.d == 0:
            other.d = 1
        else:
            pass
        star = self.n * other.d
        dontanderstend = self.d * other.n
        return '{}/{}'.format(star, dontanderstend)
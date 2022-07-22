import math

class SegmentEror:
    def __init__(self, start, end):
        if start > end:
            print('Початок відрізку більший за його кінець') 
        else:
            self.s = start
            self.e = end 

    def ret_s(self):
        return self.s

    def ret_e(self):
        return self.e              



class Segment:
    def __init__(self, a, b):
        self.a = SegmentEror(a, b).ret_s()
        self.b = SegmentEror(a, b).ret_e()
        
        self.A = []
        for i in range(self.a, self.b + 1):
            self.A.append(i)
        self.A = set(self.A)
        self.q = None

    def emp(self):
        if len(self.A) == 0:
            return 'interval is empty'
        else:
            return 'interval is not empty'

    def interval(self):
        return self.A

    def add(self, other):
        return self.A & other.A

    def str(self):
        return 'start:\n' + str(self.a) + '\nend\n' + str(self.b) + '\n' + str(self.emp()) + '\n' + str(list(self.A))


class SegmentSet():

    def intersection(self, A, B):
        return set.intersection(A, B)

    def obyednannya(self, A, B):
        return set.union(A, B)

    def diff(self, A, B):
        return set.difference(A, B)

    def sym_diff(self, A, B):
        return set.symmetric_difference(A, B)


if __name__ == '__main__':
    print('Введіть два інтервали : початок і кінець через пробіл')
    aaa = input('Перший інтервал').split(' ')
    bbb = input('Другий інтервал').split(' ')
    aa = []
    bb = []
    for i in range(int(aaa[0]), int(aaa[1]) + 1):
        aa.append(i)
    for i in range(int(bbb[0]), int(bbb[1]) + 1):
        bb.append(i)
    a = set(aa)
    b = set(bb)

    while True:
        n = input('Якщо ви хочете :\n'
                  'Знайти перетин множин введіть "*"\n'
                  'Знайти Об"єднання множин введіть "+"\n'
                  'Знайти Різницю множин введіть "-"\n'
                  'Знайти симетричну різницю введіть "/"\n'
                  'Знайти вирішення рівняння введіть "1"\n'
                  'Якшо ви хочете побачити роботу функції str введіть "@"\n'
                  'ВИЙТИ - введіть "0"')

        if n == '*':
            print(SegmentSet().intersection(a, b))
        elif n == '+':
            print(SegmentSet().obyednannya(a, b))
        elif n == '-':
            q = int(input('Якшо ви хочете від першого інтервалу відняти другий введіть "1"\n'
                          'Якщо ви хочете від другого інтервалу відняти перший введіть "2"'))
            if q == 1:
                print(SegmentSet().diff(a, b))
            elif q == 2:
                print(SegmentSet().diff(b, a))
        elif n == '/':
            Q = int(input('Якшо ви хочете  знайти симетричну різницю першого інтервалу від другого введіть "1"\n'
                          'Якшо ви хочете  знайти симетричну різницю другого інтервалу від першого введіть "2"'))
            if Q == 1:
                print(SegmentSet().sym_diff(a, b))
            elif Q == 2:
                print(SegmentSet().sym_diff(b, a))
        elif n == '1':

            koreni = []
            print("Введите коэффициенты для уравнения")
            print("ax^2 + bx + c >= 0:")
            a = float(input("a = "))
            b = float(input("b = "))
            c = float(input("c = "))

            discr = b ** 2 - 4 * a * c

            if discr > 0:
                x1 = (-b + math.sqrt(discr)) / (2 * a)
                x2 = (-b - math.sqrt(discr)) / (2 * a)
                print("x1 = {}  \nx2 = {}".format(x1, x2))
                koreni.append(x1)
                koreni.append(x2)
            elif discr == 0:
                x = -b / (2 * a)
                koreni.append(x)
                print("x = ", x)
            else:
                print("Корней нет")

            if len(koreni) == 2:
                print('(-inf;{}]U[{};+inf)'.format(min(koreni), max(koreni)))
            elif len(koreni) == 1:
                print('[{};+inf)'.format(koreni[0]))
        elif n == '@':
            q = input('Введіть інтервал який ви хочете побачити : \n"1" - перший\n "2" - другий')
            if q == '1':
                print(Segment(int(aaa[0]), int(aaa[1])))
            elif q == '2':
                print(Segment(int(bbb[0]), int(bbb[1])))
        elif n == '0':
            break
class Car:
    def __init__(self, cost, volume, fuel, distance):
        self.km = distance
        self.cost = cost
        self.v = volume
        self.vb = fuel

    def fuel_per_km(self, p):  # p кількість пасажирів або тонн вантажу
        pass

    def cost_km(self, p, km):  # p кількість пасажирів або тонн вантажу
        pass

    def go(self, ks, fpk):
        km = self.vb + ks
        lenght = self.vb - (fpk * ks)
        return km, lenght

    def distance_to_refill(self, fpk):
        dis = self.vb / fpk
        return dis

    def get_earn(self, fpk, cost, cash, km):
        money = cash - (cost * (km * fpk))  # чистий прибуток
        return money


class Personal(Car):
    def __init__(self, cost, volume, fuel, distance, pep_max, cena):
        super().__init__(cost, volume, fuel, distance)
        self.max = pep_max
        self.cena = cena

    def fuel_per_km(self, p):
        if self.max >= p:
            fpk = (self.v / self.v - 15) * (p * 0.1)
            return fpk
        else:
            print('Кількість пасажирів надто велика для цієї машини!')

    def cost_km(self, p, km):
        cost = km * self.cena * (p * 0.1)
        return cost


class Truck(Car):
    def __init__(self, cost, volume, fuel, distance, pep_max, cena):
        super().__init__(cost, volume, fuel, distance)
        self.max = pep_max
        self.cena = cena

    def fuel_per_km(self, p):
        if self.max >= p:
            fpk = (self.v / self.v - 15) * (p * 0.25)
            return fpk
        else:
            print('Вантажопідйомність цієї машини замала!')

    def cost_km(self, p, km):
        cost = km * self.cena * (p * 0.25)
        return cost


class Buss(Car):
    def __init__(self, cost, volume, fuel, distance, pep_max, cena):
        super().__init__(cost, volume, fuel, distance)
        self.max = pep_max
        self.cena = cena

    def fuel_per_km(self, p):
        if self.max >= p:
            fpk = (self.v / self.v - 15) * (p * 0.15)
            return fpk
        else:
            print('Вантажопідйомність цієї машини замала!')

    def cost_km(self, p, km):
        cost = km * self.cena * (p * 0.1)
        return cost

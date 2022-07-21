
class Employee:

    # work time in years
    def __init__(self, position, qualification, name, study, work_time, selar, vocabulary):
        self.p = position
        self.q = qualification
        self.n = name
        self.s = study
        self.v = vocabulary
        self.w_t = work_time
        self.sel = selar

    def add_one(self):
        self.v[self.p] = {}
        self.v[self.p][self.q] = {}
        self.v[self.p][self.q][self.n] = {}
        self.v[self.p][self.q][self.n][self.w_t] = self.w_t
        self.v[self.p][self.q][self.n][self.s] = self.s
        self.v[self.p][self.q][self.n][self.sel] = self.sel
        return self.v


class Software_engineer(Employee):
    def __init__(self, position, qualification, name, study, work_time, selar, vocabulary):
        super().__init__(position, qualification, name, study, work_time, selar, vocabulary)

    def calculatesalary(self):
        g = int(self.q)
        b = int(self.sel)
        y = int(self.w_t)
        salary = g * b * (1 + (y / 10))
        return salary


class Offiсe_rat(Employee):
    def __init__(self, position, qualification, name, study, work_time, selar, vocabulary):
        super().__init__(position, qualification, name, study, work_time, selar, vocabulary)

    def calculatesalary(self):
        b = int(self.sel)
        y = int(self.w_t)
        salary = b * (1 + 0.1 * (y / 3))
        return salary


class Tester(Employee):
    def __init__(self, position, qualification, name, study, work_time, selar, vocabulary):
        super().__init__(position, qualification, name, study, work_time, selar, vocabulary)

    def calculatesalary(self):
        b = int(self.sel)
        y = int(self.w_t)
        salary = b * (1 + (y / 5))
        return salary

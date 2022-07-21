class Person:

    v = {}

    def __init__(self, sex, name_and_surname, status):
        self.status = status
        self.sex = sex
        self.name = name_and_surname

    def add_all(self):
        Person.v['appointment'] = {}
        Person.v['appointment'][self.status] = {}

        Person.v['appointment'][self.status][self.sex] = {}
        # XX чи XY пара хромосом що визначають стать
        Person.v['appointment'][self.status][self.sex] = {}

        if Person.v['appointment'][self.status][self.sex] == 'XX':
            Person.v['appointment'][self.status][self.sex]['nameless'] = self.name
        else:
            Person.v['appointment'][self.status][self.sex]['nameless'] = self.name


    def show(self):
        if self.sex == 'XX':
            equality = "жіноча"
        else:
            equality = "чоловіча"

        print('статус:' + self.status, 'cтать:' + equality, 'ім\'я:' + self.name)

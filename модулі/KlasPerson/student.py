from person import Person


class Student(Person):

    def __init__(self, sex, status, name, subject, groop, points, benef, vocabular):
        super().__init__(sex, status, name)
        self.subject = subject
        self.groop = groop
        self.points = points
        self.benef = benef
        self.vocabular = vocabular
        super().add_all()

    def add_student_to_list(self):
        if self.benef:
            if self.v['apointment'] == "Student":
                self.vocabular['group'] = self.groop
                self.vocabular['group'][self.groop] = {}
                self.vocabular['group'][self.groop][self.sex] = {}
                self.vocabular['group'][self.groop][self.sex][self.name] = {}
                self.vocabular['group'][self.groop][self.sex][self.name][self.subject] = self.points
        else:
            if self.v['appointment'] == 'SpecialStudent':
                self.vocabular['group'] = self.groop
                self.vocabular['group'][self.groop] = {}
                self.vocabular['group'][self.groop][self.sex] = {}
                self.vocabular['group'][self.groop][self.sex][self.name] = {}
                self.vocabular['group'][self.groop][self.sex][self.name][self.subject] = self.points

    def show_student(self):
        global people
        if self.sex == 'XX':
            equality = "жіноча"
        else:
            equality = "чоловіча"

        if self.status == 'Student':
            people = "Звичайний"
        elif self.status == 'SpecialStudent':
            people = "З особливими потребами"

        print('статус:' + people, 'cтать:' + equality, 'група:' + self.groop, 'ім\'я:' + self.name,
              'предмети:' + self.subject)
        print('оцінки:' + self.points)

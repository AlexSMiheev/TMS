class IntFromOneToTen:
    def __set_name__(self, owner, name):
        self.public_name = name
        self.private_name = '_' + name

    def __get__(self, instance, owner=None):
        value = getattr(instance, self.private_name)
        return value

    def __set__(self, instance, value):
        for rating in value:
            if not isinstance(rating, int) or rating < 1 or rating > 10:
                raise ValueError
        setattr(instance, self.private_name, value)


class Student:
    academic_performance = IntFromOneToTen()

    def __init__(self, last_name, first_name, group_number, academic_performance: list):
        self.last_name = last_name
        self.first_name = first_name
        self.group_number = group_number
        self.academic_performance = academic_performance

    @property
    def first_name(self):
        return self._first_name

    @first_name.setter
    def first_name(self, value):
        if isinstance(value, str):
            self._first_name = value
        else:
            raise ValueError

    @first_name.deleter
    def first_name(self):
        self._first_name = None

    @property
    def last_name(self):
        return self._last_name

    @last_name.setter
    def last_name(self, value):
        if isinstance(value, str):
            self._last_name = value
        else:
            raise ValueError

    @last_name.deleter
    def last_name(self):
        self._last_name = None

    def get_ratings(self):
        for rating in self.academic_performance:
            return rating

    def average_rating(self):
        average_rating = 0
        for rating in self.academic_performance:
            average_rating = average_rating + int(rating)
        return int(average_rating / len(self.academic_performance))


class School:
    def __init__(self, list_of_students: list):
        self.list_of_students = list_of_students

    def add_student(self, student: Student):
        self.list_of_students.append(student)

    def get_best_students(self):
        for student in self.list_of_students:
            if student.get_ratings() == 5 or student.get_ratings == 6:
                print(f'Last Name - {student.last_name} Group - {student.group_number}')

    def get_students_by_group(self, group):
        for student in self.list_of_students:
            if student.group_number == group:
                print(student.first_name, student.last_name)

    def get_students_without_exams(self):
        for student in self.list_of_students:
            if student.average_rating() >= 7:
                print(student.first_name, student.last_name)


s1 = Student('Marley', 'Boob', 1, [5, 6, 7, 8, 9])
print(s1.first_name)
print(s1.last_name)
print(s1.average_rating())
print(s1.get_ratings())

s2 = Student('Arely', 'Mark', 1, [1, 2, 3, 4, 5])
print(s2.first_name)
print(s2.last_name)
print(s2.average_rating())
print(s2.get_ratings())

sc1 = School([s1])
print(sc1.list_of_students)
sc1.add_student(s2)
print(sc1.list_of_students)
sc1.get_students_without_exams()
sc1.get_best_students()
sc1.get_students_by_group(1)

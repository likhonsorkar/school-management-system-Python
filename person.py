class Person:
    def __init__(self,name):
        self.name = name

class Teacher(Person):
    def __init__(self, name):
        super().__init__(name)

    def teach(self):
        pass
    def evaluate_exam(self):
        pass
class Students(Person):
    def __init__(self, name, classroom):
        super().__init__(name)
        self.classroom = classroom
        self.marks = {}
        self.subject_grade = {}
        self.grade = {}
    def calculate_final_grade(self):
        pass
    @property
    def id(self):
        pass
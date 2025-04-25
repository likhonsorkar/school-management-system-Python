class School:
    def __init__(self,name, address):
        self.name = name
        self.address = address
        self.teachers = {}
        self.classrooms = {}
    def add_classroom(self,classroom):
        self.classrooms[classroom.name] = classroom
    def add_teacher(self, subject, teacher):
        self.teachers[subject] = teacher
    def student_admission(self, student):
        pass
    @staticmethod
    def calculate_grade(marks):
        if 80<= marks >=100:
            return 'A+'
        elif 70<= marks >=79:
            return 'A'
        elif 60<= marks >=69:
            return 'A-'
        elif 50<= marks >=59:
            return 'B'
        elif 40<= marks >=49:
            return 'C'
        elif 33<= marks >=39:
            return 'D'
        else:
            return 'F'
    @staticmethod
    def grade_to_value(grade):
        grade_map = {
            'A+' : 5.00,
            'A'  : 4.00,
            'A-' : 3.5,
            'B'  : 3.0,
            'C'  : 2.0,
            'D'  : 1.0,
            'F'  : 0.00
        }
        return grade_map[grade]
    @staticmethod
    def value_to_grade(value):
        pass
    def __repr__(self):
        pass
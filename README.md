# 📚 School Management System

This project implements a basic **School Management System** in Python. It simulates a small academic environment with entities such as School, Classroom, Subject, Teacher, and Student.

---

## 🚀 Features

- Manage school structure: classrooms, subjects, teachers, and students.
- Simulate semester final exams and evaluate student performance.
- Dynamic grading system with GPA conversion.
- Basic extensible OOP design using inheritance and encapsulation.

---

## 🏫 Components Overview

### 1. **School**

Represents the school as a whole.

#### Attributes:
- `name`: Name of the school.
- `address`: Address of the school.
- `teachers`: Dictionary mapping subjects to teachers.
- `classrooms`: Dictionary of classroom instances.

#### Methods:
- `add_classroom(classroom)`: Adds a classroom to the school.
- `add_teacher(subject, teacher)`: Assigns a teacher to a subject.
- `student_admission(student)`: Enrolls a student into a classroom.
- `calculate_grade(marks)`: *(Static)* Calculates letter grade from marks.
- `grade_to_value(grade)`: *(Static)* Converts grade to GPA value.
- `value_to_grade(value)`: *(Static)* Converts GPA value to letter grade.
- `__repr__()`: Returns a string representation of the school and its data.

---

### 2. **ClassRoom**

Represents a specific classroom.

#### Attributes:
- `name`: Name of the classroom.
- `students`: List of enrolled students.
- `subjects`: List of subjects offered.

#### Methods:
- `add_student(student)`: Enrolls a student.
- `add_subject(subject)`: Adds a subject to the curriculum.
- `take_semester_final()`: Conducts exams for all students.
- `get_top_students()`: *(TODO)* Sorts students by academic performance.

---

### 3. **Subject**

Defines a subject and its related properties.

#### Attributes:
- `name`: Subject name.
- `teacher`: Assigned teacher.
- `max_marks`: Maximum attainable marks.
- `pass_marks`: Minimum passing marks.

#### Methods:
- `exam(students)`: Conducts exams and assigns marks.

---

### 4. **Person**

Base class for Teacher and Student.

#### Attributes:
- `name`: Person's full name.

---

### 5. **Teacher** *(inherits from Person)*

Represents a teacher entity.

#### Methods:
- `teach()`: Placeholder method for teaching functionality.
- `evaluate_exam()`: Returns random marks for student evaluation.

---

### 6. **Student** *(inherits from Person)*

Represents a student entity.

#### Attributes:
- `classroom`: Classroom the student is assigned to.
- `marks`: Dictionary of subject names to marks.
- `subject_grade`: Dictionary of subject grades.
- `grade`: Final calculated grade.

#### Methods:
- `calculate_final_grade()`: Computes the average grade from all subjects.

#### Properties:
- `id`: Get or set the student's unique ID.

---

## 🔧 Future Enhancements

- Implement `get_top_students()` to rank students.
- Add persistence (file/database storage).
- Introduce GUI or web interface for interaction.
- Improve grading policies with weights and GPA scales.

---

## 🧪 How to Run

```bash
python main.py
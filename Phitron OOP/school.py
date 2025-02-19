class Student:
    def __init__(self, name, age, id):
        self.name = name
        self.age = age
        self.id = id
        
class Courses:
    def __init__(self, name, teacher):
        self.name = name
        self.teacher = teacher
        
class Teacher:
    def __init__(self,name, course):
        self.name = name
        self.course = course

class School:
    def __init__(self,name, teachers, courses, students):
        self.name = name
        self.teachers = teachers
        self.courses = courses
        self.students = students
        
    def get_student(self):
        for student in self.students:
            print(student.name)

School_Name = 'Phitron'

ds_course = Courses("Data Structure", "Selim")
teacher_1 = Teacher("Selim", ds_course)

algo_course = Courses("Algorithm", "Sefat")
teacher_2 = Teacher("Sefat", algo_course)

student_1 = Student("Nahin", 17, 2027)
student_2 = Student("Ahad", 19, 2051)
student_3 = Student("Tusher", 89, 2020)

courses = [ds_course, algo_course]
teachers = [teacher_1, teacher_2]

students = [student_1, student_2, student_3]

my_school = School(School_Name, teachers, courses, students)
my_school.get_student()
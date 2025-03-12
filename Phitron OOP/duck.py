# Duck Typing
class Teacher:
    def __init__(self, name):
        self.teacherName = name
        self.stuents = []
    def entry_students(self, studentObj):
        self.stuents.append(studentObj)

class Student(Teacher):
    def __init__(self, name):
        self.studnetName = name
        Teacher.__init__(self, "Selim Reza")
        Teacher.entry_students(self, self)
    def enter_in_a_teacher(self, teacherObj):
        teacherObj.stuents.append(self)  
    def __repr__(self):
        return f"Student({self.studnetName})"
solaiman_mia = Teacher("Solaiman Mia")
rahim_mia = Teacher("Rahim Mia")
ms_rahima = Teacher("Ms Rahima")
student1 = Student("Saba")
student2 = Student("Selim")
student1.enter_in_a_teacher(rahim_mia)
student2.enter_in_a_teacher(ms_rahima)

print(rahim_mia.stuents)
print(ms_rahima.stuents)
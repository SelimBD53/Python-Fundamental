# MRO == Method Resolation Order
class School:
    def __init__(self, name):
        self.schoolName = name
    def __repr__(self):
        return f"School({self.schoolName})"
        
class Teacher:
    def __init__(self, name):
        self.teacherName = name
    def __repr__(self):
        return f"Teacher({self.teacherName})"
class Student(Teacher, School):
    def __init__(self, name, teacherName, schoolName):
        Teacher.__init__(self, teacherName)
        School.__init__(self, schoolName)
        # super().__init__(teacherName)
        # super().__init__(schoolName)
        self.studentName = name
    def __repr__(self):
        return f"Student({self.studentName})"
    

student = Student("Selim", "Tanpia Tasnim", "Green View")
print(student.teacherName, student.schoolName)
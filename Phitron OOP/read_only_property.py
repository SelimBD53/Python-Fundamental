class Student:
    def __init__(self, name, id, mark):
        self._name = name
        self.__id = id
        self.mark = mark
    @property
    def student_id(self):
        return self.__id
    @property
    def name(self):
        return self._name
    @name.deleter
    def name(self):
        del self._name
        
selim = Student("Selim Reza", 15, 22)
print(selim.student_id)
selim.__id = 44
print(dir(selim))
print(selim.student_id)
print(selim.name)
# del selim._name
print(selim._name)
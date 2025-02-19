class Employee:
    def __init__(self, name, password, phone):
        self.name = name
        self.__password = password
        self.__phone = phone
    def __get_password(self):
        return self.__password

my_employee = Employee("Selim", "DataEntry", "017989865")
# print(my_employee.phone)
# print(my_employee.password)
# print(my_employee._Employee__get_password())
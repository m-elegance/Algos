class Student:
    def __init__(self, name, group, age):
        self.name = name
        self.group = group
        self.age = age

    def print_info_student(self):
        print(self.name)
        print(self.group)
        print(self.age)


a = Student("Marat", "05-101", 20)
a.print_info_student()



class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        return f"Hello, {self.name}"


student = Student("Ali", 20)

print(type(student))
print(id(student))
print(dir(student))
print(isinstance(student, Student))
help(student)
from abc import abstractmethod

class Skoll:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @abstractmethod
    def Print(self):
        print(f"Name: {self.name} \nAge: {self.age}")



class Teaher(Skoll):
    def __init__(self, name, age, salary):
        Skoll.__init__(self, name, age)
        self.salary = salary

    def Print(self):
        Skoll.Print(self)
        print(f"Salary: {self.salary} \n")


class Student(Skoll):
    def __init__(self, name, age, marks):
        Skoll.__init__(self, name, age)
        self.marks = marks

    def Print(self):
        Skoll.Print(self)
        print(f"Marks: {self.marks} \n")

t = Teaher("M", 23, 10000)
s = Student("S", 26, 1000)

m = [t, s]

for i in m:
    i.Print()
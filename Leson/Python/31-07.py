import abc

class Person(abc.ABC):
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    @property # set of name
    def name(self):
        return self.__name
    @name.setter
    def name(self, name):
        self.__name = name
    
    @property # set of age
    def age(self):
        return self.__age
    @age.setter
    def age(self, age):
        self.__age = age

    def __str__(self):
        return f'Name: {self.__name}\nAge: {self.__age}'
    
    @abc.abstractmethod
    def Work(self):
        pass

class Student(Person):
    def __init__(self, name, age, academy):
        super().__init__(name, age)
        self.__academy = academy
    
    def __str__(self):
        return super().__str__() + f'\nAcademy: {self.__academy}\n'

    def Work(self):
        return f'{self.name} studies on {self.__academy}'
    
class Teacher(Person):
    def __init__(self, name, age, school, subject):
        super().__init__(name, age)
        self.__school = school
        self.__subject = subject

    def __str__(self):
        return super().__str__() + f'\nSchool: {self.__school}\nSubject: {self.__subject}\n'
    
    def Work(self):
        return f'{self.name} work in {self.__school} and teaches {self.__subject}'
    
class Doctor(Person):
    def __init__(self, name, age, specialization):
        super().__init__(name, age)
        self.__specialization = specialization

    def __str__(self):
        return super().__str__() + f'\nSpecialization: {self.__specialization}\n'

    def Work(self):
        return f'{self.name} working {self.__specialization}'
    
def PrintWork(gpoup):
    for i in gpoup:
        print(i.Work())

def main():
    group = [Student('Oleg', 18, 'IT STEP'), Teacher('Vlad', 24, 'IT STEP', 'C++'), Doctor('Daria', 21, 'Dentist')]
    PrintWork(group)
main()
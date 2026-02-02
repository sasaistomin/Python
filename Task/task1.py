import abc
class Person:
    def __init__(self, name, address):
        self.address = address
        self.name = name

    @abc.abstractmethod
    def Print(self):
        print(f"Your name: {self.name}\nYour address: {self.address}")

class Admin(Person):
    def __init__(self, name, address, salary):
        Person.__init__(self, name, address)
        self.salary = salary

    def Print(self):
        print("Info Admin")
        Person.Print(self)
        print(f"Your salary: {self.salary}\n")

class Customer(Person):
    def __init__(self, name, address, cost):
        Person.__init__(self, name, address)
        self.cost = cost

    def Print(self):
        print("Info Customer")
        Person.Print(self)
        print(f"Your cost: {self.cost}\n")

a = Admin("Sasha", "Odess", 10000)
a.Print()

c = Customer("Oleg", "Odess", 5000)
c.Print()
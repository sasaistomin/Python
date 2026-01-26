from abc import abstractmethod

class Person:
    def __init__(self, name, adres):
        self.name = name
        self.adres = adres

    @abstractmethod
    def Print(self):
        print(f"Your name {self.name}\nYour adress {self.adres}")

class Admin(Person):
    def __init__(self, name, adres, salary):
        Person.__init__(self, name, adres)
        self.salary = salary

    def Print(self):
        Person.Print(self)
        print(f"Your salary {self.salary}\n")

class Customer(Person):
    def __init__(self, name, adres, cost):
        Person.__init__(self, name, adres)
        self.cost = cost

    def Print(self):
        Person.Print(self)
        print(f"Your must pay {self.cost}")


a = Admin("Admin", "Odessa", 100)
b = Customer("Customer", "Kiev", 200)

a.Print()
b.Print()

class Person:
    def __init__(self, name):
        self.name = name

    def Hello(self):
        print(self.name)

p = Person("Sasha")
p.Hello()
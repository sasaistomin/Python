class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email

    def Greet(self):
        print(f"Hello {self.name}, your email {self.email}")

u = User("Sasha", "sasaistomin42@gmail.com")
u.Greet()
class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def __str__(self):
        return f"Name: {self.name}, Price: {self.price}"

    def __len__(self):
        return self.quantity

    def __eq__(self, other):
        if not isinstance(other, Product):
            return False
        return self.name == other.name and self.price == other.price

p1 = Product("Ноутбук", 50000, 5)
p2 = Product("Ноутбук", 50000, 10)
p3 = Product("Мышь", 1500, 2)

print(str(p1))
print(len(p1))
print(p1 == p2)
print(p1 == p3)
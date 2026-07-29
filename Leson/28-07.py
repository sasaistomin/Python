# Реалізуйте клас «Годинник». Збережіть у класі: назву моделі годинника, виробника годинника, рік випуску, ціну годинника, тип годинника (наручний, настінний і т.д.). 
# Реалізуйте конструктор та методи класу для введення-виведення даних, а також для інших операцій. Використовуйте механізм перевантаження методів.
class Clok: 
    def __init__(self, name, whyDo, price):
        self.__name = name
        self.__whyDo = whyDo
        self.__price = price
    
    def __str__(self):
        return(f'Name: {self.__name}\nWhy do: {self.__whyDo}\nPrice: {self.__price}')
    
    def __isub__(self, other):
        self.__price -=other
        return self
    
    def __add__(self, other):
        n = Clok('re', 'qw', self.__price + other.__price)
        return n
    
    @property
    def price(self):
        return self.__price
    @price.setter
    def price(self, price):
        self.__price = price
    
def main():
    c = Clok('Pagani Design PD-1794M Silver-Blue', 'Pagani', 3335)
    print(c)
    c.price = 500
    print(c)
    a = Clok('N', 'r', 1000)
    b = c + a
    print(b)
    # c -= 500
    # print(c)
main()        
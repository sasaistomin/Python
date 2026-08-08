class Person:
    def __init__(self, fullName, date, phone, city, canti, adres):
        self.__fullName = fullName
        self.__date = date
        self.__phone = phone # do property
        self.__city = city  # do property
        self.__canti = canti # do property
        self.__adres = adres # do property
        
    def __str__(self):
        return f'Name: {self.__fullName}\nDate: {self.__date}\nPhone: {self.__phone}\nCity: {self.__city}\nCntri: {self.__canti}\nAdres: {self.__adres}'
    
    
class City:
    def __init__(self, name, rigion, nameCantri, countPiople, postIndex, phoneCode):
        self.__name = name
        self.__rigion = rigion
        self.__nameCantri = nameCantri
        self.__countPiople = countPiople # do property
        self.__postIndex = postIndex
        self.__phoneCode = phoneCode

    def __str__(self):
        return f'Name: {self.__name}\nRigion: {self.__rigion}\nCantri: {self.__nameCantri}\nCount piople: {self.__countPiople}\nPost index: {self.__postIndex}\nPhone code: {self.__phoneCode}'
    
    def __eq__(self, other):
        if isinstance(other, City):
            return self.__countPiople == other.__countPiople
        return NotImplemented

    def __lt__(self, other):
        if isinstance(other, City):
            return self.__countPiople < other.__countPiople
        return NotImplemented

    def __gt__(self, other):
        if isinstance(other, City):
            return self.__countPiople > other.__countPiople
        return NotImplemented

    def __add__(self, amount: int):
        if isinstance(amount, int):
            return City(self.__name, self.__rigion, self.__nameCantri, 
                        self.__countPiople + amount, self.__postIndex, self.__phoneCode)
        return NotImplemented

    def __sub__(self, amount: int):
        if isinstance(amount, int):
            return City(self.__name, self.__rigion, self.__nameCantri, 
                        max(0, self.__countPiople - amount), self.__postIndex, self.__phoneCode)
        return NotImplemented

class Cntri: 
    def __init__(self, name, nameC, countPiople, phoneCantri, nameMainCity, nameCity=None):
        self.__name = name
        self.__nameC = nameC
        self.__countPiople = countPiople
        self.__phoneCantri = phoneCantri
        self.__nameMainCity = nameMainCity
        self.__nameCity = nameCity if nameCity is not None else []

    def __str__(self):
        return (f'Name: {self.__name}\nContinent: {self.__continent}\n'
                f'Count piople: {self.__countPiople}\nPhone code: {self.__phoneCantri}\n'
                f'Main city: {self.__nameMainCity}\n')

class Website:
    def __init__(self, name, url, description):
        self.__name = name
        self.__url = url
        self.__description = description

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    @property
    def url(self):
        return self.__url

    @url.setter
    def url(self, value):
        self.__url = value

    @property
    def description(self):
        return self.__description

    @description.setter
    def description(self, value):
        self.__description = value

    def __str__(self):
        return f"Website: {self.__name}\nURL: {self.__url}\nDescription: {self.__description}"

class Car:
    def __init__(self, model, year, manufacturer, engine_capacity, color, price):
        self.__model = model
        self.__year = year
        self.__manufacturer = manufacturer
        self.__engine_capacity = engine_capacity
        self.__color = color
        self.__price = price
    def __str__(self):
        return (f"Модель: {self.__model}\nРік випуску: {self.__year}\nВиробник: {self.__manufacturer}\n"
                f"Об'єм двигуна: {self.__engine_capacity}л\nКолір: {self.__color}\nЦіна: ${self.__price:.2f}")
    
class Book:
    def __init__(self, title, year, publisher, genre, author, price):
        self.__title = title
        self.__year = year
        self.__publisher = publisher
        self.__genre = genre
        self.__author = author
        self.__price = price

    def __str__(self):
        return (f"Назва: «{self.__title}»\nАвтор: {self.__author}\nРік видання: {self.__year}\n"
                f"Жанр: {self.__genre}\nВидавець: {self.__publisher}\nЦіна: {self.__price:.2f} грн")

class Stadium:
    def __init__(self, name, opening_date, country, city, capacity):
        self.__name = name
        self.__opening_date = opening_date
        self.__country = country
        self.__city = city
        self.__capacity = capacity  
          
    def __str__(self):
        return (f"Стадіон: {self.__name}\nДата відкриття: {self.__opening_date}\n"
                f"Країна: {self.__country}\nМісто: {self.__city}\nМісткість: {self.__capacity} глядачів")

def main():
    pass
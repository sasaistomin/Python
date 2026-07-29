class Person:
    def __init__(self, fullName, date, phone, city, canti, adres):
        self.__fullName = fullName
        self.__date = date
        self.__phone = phone
        self.__city = city
        self.__canti = canti
        self.__adres = adres
        
    def __str__(self):
        return f'Name: {self.__fullName}\nDate: {self.__date}\nPhone: {self.__phone}\nCity: {self.__city}\nCntri: {self.__canti}\nAdres: {self.__adres}'
    
    
    
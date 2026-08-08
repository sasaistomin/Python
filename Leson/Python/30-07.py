class Transport: 
    def __init__(self, name, oil):
        self.__name = name
        self.__oil = oil
    
    def __str__(self):
        return f'Name: {self.__name}\nOil: {self.__oil}'
    
    def disp(self):
        return f'Name: {self.__name}\nOil: {self.__oil}'

class Auto(Transport):
    def __init__(self, name, oil, maxSpid, number):
        super().__init__(name, oil)
        self.__maxSpid = maxSpid
        self.__number = number

    def __str__(self):
        return f'Name: {self.__name}\nOil: {self.__oil}\nMax spid: {self.__maxSpid}\nNumber: BH{self.__number}OA'

    def disp(self):
        return super().disp() + f'Max spid: {self.__maxSpid}\nNumber: BH{self.__number}OA'
    
    @property
    def number(self):
        return self.__number
    @number.setter
    def number(self, number):
        self.__number = number

    @property
    def maxSpid(self):
        return self.__maxSpid
    @maxSpid.setter
    def maxSpid(self, maxSpid):
        self.__maxSpid = maxSpid

def main():
    t = Transport('BMV', 'Benzin')
    t.disp()
    a = Auto('Mersedes', 'Dizel', 300, 3034)
    print(a.disp())


main()
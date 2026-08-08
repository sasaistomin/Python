class Auto:
    def __init__(self, name, dateOfDo, spid, ves, countL):
        self.__name = name
        self.__dateOfDo = dateOfDo
        self.__spid = spid
        self.__ves = ves
        self.__countL = countL
    def Print(self):
        print(f'Name: {self.__name}\nDate: {self.__dateOfDo}\nMax spid: {self.__spid} k-m\nVes: {self.__ves} kg\nCount petrol: {self.__countL} l')
        
    @property
    def name(self): # Get
        return self.__name
    @name.setter # Set
    def name(self, name):
        self.__name = name
        
    @property
    def dateOfDo(self): # Get
        return self.__dateOfDo
    @dateOfDo.setter # Set
    def dateOfDo(self, dateOfDo):
        self.__dateOfDo = dateOfDo
        
    @property
    def spid(self): # Get
        return self.__spid 
    @spid.setter # Set
    def spid(self, spid):
        self.__spid = self.spid
        
    @property
    def ves(self): # Get 
        return self.__ves
    @ves.setter # Set
    def ves(self, ves):
        self.__ves = ves
    
    @property
    def countL(self): # Get
        return self.__countL
    @countL.setter # Set
    def countL(self, countL):
        self.__countL = self.countL
    
def Main():
    a = Auto('Car', '10.05.2021', 230, 4500, 60)
    a.Print()

Main()
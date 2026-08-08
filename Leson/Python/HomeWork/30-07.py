# Задание 1
# Создать абстрактный базовый класс с абстрактной функцией - корни уравнения. 
# Создать производные классы: класс линейных уравнений и класс квадратных уравнений. 
# Определить функцию вычисления корней уравнений.
import abc

class AbstrackClass(abc.ABC):
    @abc.abstractmethod
    def solc(self):
        pass


class LinearEquation(AbstrackClass):
    def __init__(self, a, b):
        self.__a = a
        self.__b = b
    
    def solc(self):
        if self.__a == 0:
            if self.__b == 0:
                return '+_+'
            else:
                return 'Erorr'
        
        x = -self.__b / self.__a 
        return f'Result: {x}'

class QuadraticEquation(AbstrackClass):
    def __init__(self, a, b, c):
        self.__a = a
        self.__b = b
        self.__c = c 
    
    @staticmethod  
    def sqrt(num):
        if num < 0:
            raise ValueError('Erorr')
        if num == 0:
            return 0
        
        xN = num
        e = 1e-10

        while True:
            nextN = 0.5 * (xN + num / xN)

            if abs(xN - nextN) < e:
                return nextN
            
            xN = nextN 

    def solc(self):
        if self.__a == 0:
            l = LinearEquation(self.__b, self.__c)
            return l.solc()
            
        d = self.__b**2 - 4 * self.__a * self.__c

        if d > 0:
            x1 = (-self.__b + self.sqrt(d)) / (2 * self.__a)
            x2 = (-self.__b - self.sqrt(d)) / (2 * self.__a)
            return f'X1: {x1}\nX2: {x2}'
            
        elif d == 0:
            x = -self.__b / (2 * self.__a)
            return f'X: {x}'
        else:
            return 'Not result (D < 0)'


def main():
    equations = [
        LinearEquation(a=2, b=-4),       
        LinearEquation(a=0, b=5),  
        QuadraticEquation(a=1, b=-5, c=6)
    ]

    for eq in enumerate(equations, 1):
        print(eq.solc())
main()

# Задание 2
# Создать абстрактный базовый класс с абстрактной функцией - площадь. 
# Создать производные классы: прямоугольник, круг, прямоугольный треугольник, трапеция - со своими функциями площади. 
# Для проверки определить массив объектов на абстрактный класс, которым присваиваются адреса различных объектов.

class Square(abc.ABC):
    @abc.abstractmethod
    def solcSquare(self):
        pass


class Rectangle(Square):
    def __init__(self, a, b):
        self.__a = a
        self.__b = b
    
    def solcSquare(self):
        s = self.__a * self.__b
        return f'S Rectangle: {s}'
    
class Circle(Square):
    __p = 3.14
    def __init__(self, r):
        self.__r = r
    
    def solcSquare(self):
        s = self.__p * self.__r**2
        return f'S Circle: {s}'
    
class RightAngledTriangle(Square):
    def __init__(self, a, b):
        self.__a = a
        self.__b = b
    
    def solcSquare(self):
        s = (self.__a * self.__b) / 2
        return f'S RightAngledTriangle: {s}'
    
class Trapezoid(Square):
    def __init__(self, a, b, h):
        self.__a = a
        self.__b = b
        self.__h = h
    def solcSquare(self):
        s = ((self.__a + self.__b) / 2) * self.__h
        return f'S Trapezoid: {s}'
    
def main():
    shapes: list[Square] = [
        Rectangle(5, 10),
        Circle(4),
        RightAngledTriangle(3, 4),
        Trapezoid(6, 10, 5)
    ]
    
    for shape in shapes:
        print(shape.solcSquare())

main()
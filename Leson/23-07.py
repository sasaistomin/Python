def Sum(a,b): 
    return a+b
def Mul(a,b):
    return a*b
def Dilenie(a,b):
    return a/b
def Otnimanie(a,b):
    return a-b
def main():
    #test
    # print(InputNumber())
    number1 = float(input('Enter number1: '))
    number2 = float(input('Enter number2: '))
    char = input("Enter doing: ")
    if char == '+':
        print(Sum(number1, number2))
    elif char == '-':
        print(Otnimanie(number1, number2))
    elif char == '*':
        print(Mul(number1, number2))
    elif char == '/':
        print(Dilenie(number1, number2))
    
main()
# Калькулятор
number1 = float(input("Enter number1: "))
number2 = float(input("Enter number2: "))
znac = input("Enter char: ")

if znac == '+': 
    print(f'{number1} + {number2} = {number1+number2}')
elif znac == '-':
    print(f'{number1} - {number2} = {number1-number2}')
elif znac == '*':
    print(f'{number1} * {number2} = {number1*number2}')
elif znac == '/':
    print(f'{number1} / {number2} = {number1/number2}')
else: print("Enter corecr znac")


str1 = 'Hello World'
for i in range(len(str1)-1, -1, -1):
    print(str1[i], end='')
print()
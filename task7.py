def Kall(num1, num2, do):
    if do == "+":
        return num1 + num2
    elif do == "-":
        return num1 - num2
    elif do == "*":
        return num1 * num2
    elif do == "/":
        return num1 / num2
    else:
        print("Erorr")

number1 = int(input("Enter number1: "))
number2 = int(input("Enter number2: "))
do = input("Enter what you want to do: ")

print(Kall(number1, number2, do))
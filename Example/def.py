def MaxNumber(num1 , num2):
    if num1 > num2:
        return num1
    else:
        return num2

print("You mast enter two numbers")
numFirstMax = int(input("Enter number1: "))
numSecondMax = int(input("Enter number2: "))

print(f"Max number {MaxNumber(numFirstMax, numSecondMax)}")
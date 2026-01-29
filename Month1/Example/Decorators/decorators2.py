def add(num1, num2):
    return num1 + num2

def Sum(func, num1, num2):
    return func(num1, num2)

result = Sum(add, 11, 23)
print(result)


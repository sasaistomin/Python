def Log(func):
    def add(*args, **kwargs):
        print(f"Name: {func.__name__}")

        result = func(*args, **kwargs)
        print(f"Result: {result}")

        return result
    return add

@Log
def Sum(num1, num2):
    return num1 + num2

Sum(1, 4)
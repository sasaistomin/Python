def outer(x):
    def inner(y):
        return x + y
    return inner

add_five = outer(4)
result = add_five(4)
print(result)
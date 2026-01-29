def Generators(num):
    values = 0

    while values < num:
        yield values
        values += 1

for values in Generators(10):
    print(values)
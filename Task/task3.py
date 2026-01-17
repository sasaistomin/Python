age = int(input("Enter your age: "))

if age >= 18:
    print("You are adult")
elif age >= 10 and age <=17:
    print("You are teenager")
elif age >= 0 and age <= 9:
    print("You are child")
elif age <= -1:
    print("Error")

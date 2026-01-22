dict = { # do dict
    "Sasha": "+380660643466"
}

print(f"Phone Sasha: {dict["Sasha"]}") # print value
print(f"In book phone {len(dict)} number") # print count number id book

for name, phone in dict.items():
    print(f"Name: {name}, phone number: {phone}") # print all number in book

dict["Varya"] = "+380970374316" # add new key and value
print(f"\nNow in book phone {len(dict)} number\n")

for name, phone in dict.items():
    print(f"Name: {name}, phone number: {phone}")
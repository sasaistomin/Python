text = "Чтобы посчитать количество символов в тексте на Python, используйте встроенную функцию len(), которая возвращает общую длину строки, включая пробелы, знаки препинания и специальные символы, считая их за один символ. "

f = open("test.txt", "w")
f.write(text)
f.close()

f = open("test.txt", "r")
while True:
    line = f.readline()
    if len(line) == 0:
        break
    print(len(line))
f = open("open.txt", 'w')
f.write("Hello")
f.close()

f = open("open.txt", 'r')
while True:
    line = f.readline()
    if len(line) == 0:
        break
    print(line, end='')

f.close()
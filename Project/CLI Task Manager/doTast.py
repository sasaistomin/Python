taskList = []

def DoTast():
    print("Напишите задачу.\nЕсли хотите прекратить напишите \"Выход\"")
    while True:
        task = input("Напишите задачу: ")
        if task == "Выход":
            break
        if task:
            taskList.append(task)
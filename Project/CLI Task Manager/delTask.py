import doTast

def DeleteTask():
    print("Удаление задач")
    print("1) Удалить все задачи")
    print("2) Удалить какуют-то задачу")
    do = int(input("Выберите что хотите сделать: "))

    if do == 1:
        doTast.taskList.clear()
    elif do == 2:
        numberTask = int(input("Какую задачу вы хотите удать: "))
        index = numberTask - 1
        del doTast.taskList[index]
        print(f"Задача {numberTask}")


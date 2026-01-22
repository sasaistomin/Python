import doTast
import delTask
import printTask


while True:
    print("\nПривет, что ты хочешь сделать?")
    print("1) Посмотреть задачи")
    print("2) Добавить задачи")
    print("3) Удалить задачи")
    print("4) Выход")
    do = int(input("Введи что ты хочешь сделать: "))
    print("\n")

    if do == 1:
        printTask.Print()
    elif do == 2:
        doTast.DoTast()
    elif do == 3:
        delTask.DeleteTask()
    elif do == 4:
        break
    else:
        print("Ошибка")
        continue
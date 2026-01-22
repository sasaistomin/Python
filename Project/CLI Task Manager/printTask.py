import doTast

def Print():
    i = 1

    for task in doTast.taskList:
        print(f"{i}. {task}")
        i += 1
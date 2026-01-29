class Robot:
    countRobot = 0

    def __init__(self, name):
        self.name = name
        Robot.countRobot += 1

    def __del__(self):
        print(f"I am delete {self.name}")
        Robot.countRobot -= 1

        if Robot.countRobot == 0:
            print("Robot is empty")
        else:
            print(f"Count robot {Robot.countRobot}")

    def Hello(self):
        print(f"Hello my name is {self.name}")

    def Count():
        print(f"We have {Robot.countRobot} robots")

    Count = staticmethod(Count)

robot1 = Robot("Robot1")
robot1.Hello()
Robot.Count()

robot2 = Robot("Robot2")
robot2.Hello()
Robot.Count()

del robot1
del robot2
Robot.Count()
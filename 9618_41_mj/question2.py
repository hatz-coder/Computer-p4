class Balloon:
    def __init__(self, defenceitem1, colour1):
        self.__defenceitem = defenceitem1
        self.__colour = colour1
        self.__health = 100

    def GetDefenceItem(self):
        return self.__defenceitem

    def ChangeHealth(self, health):
        self.__health -= health

    def CheckHealth(self):
        if self.__health <= 0:
            return True
        else:
            return False


def Defend():
    Balloon1 = Balloon("Shield", "Red")
    strength = int(input("Enter The Strength of the opponent: "))
    Balloon1.ChangeHealth(strength)
    print(Balloon1.GetDefenceItem())
    if Balloon1.CheckHealth() == True:
        print("It has no health remaining")
    else:
        print("It has some health remaining")
    return Balloon1


Defend()

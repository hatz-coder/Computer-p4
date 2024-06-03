class HiddenBox:
    # PRIVATE boxname :STRING
    # PRIVATE Creator : STRING
    # PRIVATE DateHidden : STRING
    # PRIVATE GameLocation : STRING
    # PRIVATE LastFinds : ARRAY[0:9,0:1] OF STRING
    # PRIVATE Active : BOOLEAN
    def __init__(self, BN, C, Dhidden, Location):
        self.__BoxName = BN
        self.__Creator = C
        self.__DateLocation = Dhidden
        self.__GameLocation = Location
        self.__Active = False
        self.__LastFinds = [[""] * 2 for i in range(10)]

    def GetBoxName(self):
        return self.__BoxName

    def GetGameLocation(self):
        return self.__GameLocation


Theboxes = [HiddenBox("", "", "", "") for i in range(10000)]


def NewBox(Theboxes):
    userName = input("Enter BoxName: ")
    usercreator = input("enter creator: ")
    userlocation = input("enter game location : ")
    userdate = input("enter date hidden: ")
    Theboxes.append(HiddenBox(userName, usercreator, userdate, userlocation))


NewBox(Theboxes)


class PuzzleBox(HiddenBox):
    def __init__(self, BN, Creator, DateHidden, GameLocation, PuzzleText, Solution):
        super.__init__(BN, Creator, DateHidden, GameLocation)
        self.__PuzzleText = PuzzleText
        self.__Solution = Solution

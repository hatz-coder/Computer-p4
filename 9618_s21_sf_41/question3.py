class TreasureChest:
    # Private Question as String
    # Private Answer as Integer
    # Private Points as Integer
    def __init__(self, question1, answer1, points1):
        self.__Question = question1
        self.__Answer = answer1
        self.__Points = points1

    def GetQuestion(self):
        return self.__Question

    def checkAnswer(
        self,
        userans,
    ):
        if userans == self.__Answer:
            return True
        else:
            return False

    def GetPoints(self, attempts):
        if attempts == 1:
            return self.__Points
        elif attempts == 2:
            return self.__Points / 2
        elif attempts == 3 or attempts == 4:
            return self.__Points / 4
        else:
            return 0


arrayTreasure = [" "] * 5
FileName = "TreasureChestData.txt"


def ReadData():
    global arrayTreasure
    try:
        File = open(FileName, "r")
        for x in range(5):
            question = File.readline().strip()
            answer = int(File.readline().strip())
            points = int(File.readline().strip())
            arrayTreasure[x] = TreasureChest(question, answer, points)
        File.close()
    except:
        print("File Not found")


ReadData()
questionnum = 0

while questionnum < 1 or questionnum > 5:
    questionnum = int(input("Enter the question number: "))
print(arrayTreasure[questionnum - 1].GetQuestion())
correct = False
attempts = 0
while correct != True:
    correct = arrayTreasure[questionnum - 1].checkAnswer(
        int(input("Enter the answer here: "))
    )
    print(correct)
    attempts += 1
print(arrayTreasure[questionnum - 1].GetPoints(attempts))

class Card:
    def __init__(self, number, colour):
        self.__CardNumber = number
        self.__CardColour = colour

    def GetNumber(self):
        return self.__CardNumber

    def GetColour(self):
        return self.__CardColour


CardArray = [" "] * 30
print(CardArray)

File = open("CardValues.txt", "r")
for x in range(0, 30):
    Line1 = File.readline().strip()
    Line2 = File.readline().strip()
    Line = Card(Line1, Line2)
    CardArray[x] = Line
    # print(Line)

# print(CardArray[1].GetColour())
# print(CardArray[1].GetNumber())

CardsSelected = [" "] * 4

z = 0


def ChooseCard():
    global CardsSelected
    global CardArray
    global z
    number = int(input("Enter a number"))
    if number >= 0 and number < 30:
        print("cardno.", number)
        if number == CardsSelected[0]:
            ChooseCard()
        elif number == CardsSelected[1]:
            ChooseCard()
        elif number == CardsSelected[2]:
            ChooseCard()
        elif number == CardsSelected[3]:
            ChooseCard()
        else:
            # print("z value ", z)
            CardsSelected[z] = number
            z += 1
            print("Card Selected")
            print(CardsSelected)
            return number
    else:
        return False


Player1 = [" "] * 4
for x in range(0, 4):
    print("Select a integer number of card: ")
    print(ChooseCard())
for x in range(len(CardsSelected)):
    temp = Card(
        CardArray[CardsSelected[x]].GetNumber(), CardArray[CardsSelected[x]].GetColour()
    )
    Player1[x] = temp

for x in range(len(Player1)):
    print(Player1[x].GetNumber())
    print(Player1[x].GetColour())

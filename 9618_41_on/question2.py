class Card:

    def __init__(self, number1, color1):
        self.__Number = number1  # Number as Integer
        self.__Color = color1  # Color as String

    def GetNumber(self):
        return self.__Number

    def GetColor(self):
        return self.__Color


Card1 = Card(1, "red")
Card2 = Card(2, "red")
Card3 = Card(3, "red")
Card4 = Card(4, "red")
Card5 = Card(5, "red")
Card6 = Card(1, "blue")
Card7 = Card(2, "blue")
Card8 = Card(3, "blue")
Card9 = Card(4, "blue")
Card10 = Card(5, "blue")
Card11 = Card(1, "yellow")
Card12 = Card(2, "yellow")
Card13 = Card(3, "yellow")
Card14 = Card(4, "yellow")
Card15 = Card(5, "yellow")


class Hand:
    def __init__(self, Card1, Card2, Card3, Card4, Card5):

        self.__Cards = []  # Cards[10] as Card
        self.__Cards.append(Card1)
        self.__Cards.append(Card2)
        self.__Cards.append(Card3)
        self.__Cards.append(Card4)
        self.__Cards.append(Card5)
        self.__FirstCard = 0  # FirstCard as Integer
        self.__NumberCards = 5  # NumberCards as Integer

    def GetCard(self, index):
        return self.__Cards[index]


Player1 = Hand(Card1, Card2, Card3, Card4, Card11)
Player2 = Hand(Card12, Card13, Card14, Card15, Card6)


def CalculateValues(Cards):
    playerscore = 0
    for x in range(5):
        CurrentCard = Cards.GetCard(x)
        if CurrentCard.GetColor() == "red":
            playerscore += 5
        elif CurrentCard.GetColor() == "blue":
            playerscore += 10
        else:
            playerscore += 15
    return playerscore


if CalculateValues(Player1) == CalculateValues(Player2):
    print("The game resulted in draw")
elif CalculateValues(Player1) > CalculateValues(Player2):
    print("Player 1 wins with the score of", CalculateValues(Player1))
else:
    print("Player 2 wins with the score of", CalculateValues(Player2))

# Declare Player : ARRAY [1:10,0:1] OF STRING
Player = [[""] * 2 for i in range(11)]


def ReadHighScore():
    File = open("Highscore.txt", "r")
    for x in range(0, 10):
        Player[x][0] = File.readline().strip()
        Player[x][1] = File.readline().strip()
    File.close()


def OutputScores():
    for x in range(0, 11):
        print(Player[x][0], Player[x][1])


ReadHighScore()
OutputScores()
NewPlayerName = ""
NewPlayerScore = 0

while len(NewPlayerName) != 3:
    NewPlayerName = input("Enter the name of the player : ")

while NewPlayerScore <= 1 or NewPlayerScore >= 100000:
    NewPlayerScore = int(input("Enter the score of the player : "))
Player[10][0], Player[10][1] = NewPlayerName, NewPlayerScore


def BubbleSort():
    for z in range(len(Player)):
        swapped = False
        for i in range(len(Player) - 1):
            if int(Player[i][1]) < int(Player[i + 1][1]):
                temp = Player[i][1]
                nametemp = Player[i][0]
                Player[i][1] = Player[i + 1][1]
                Player[i][0] = Player[i + 1][0]
                Player[i + 1][1] = temp
                Player[i + 1][0] = nametemp
                swapped = True
        if not swapped:  # If the list is already sorted, then break the loop
            break
    return Player


OutputScores()
print("")
BubbleSort()
OutputScores()


def WriteName():
    NewFile = open("NewHighScore.txt", "w")
    for x in range(0, 10):
        line = str(Player[x][0]) + " " + str(Player[x][1]) + "\n"
        NewFile.writelines(line)


WriteName()

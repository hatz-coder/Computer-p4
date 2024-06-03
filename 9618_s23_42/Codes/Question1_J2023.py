# DECLARE Animals : ARRAY[0:9] OF STRING
global Animals
Animals = []

Animals.append("horse")
Animals.append("lion")
Animals.append("rabbit")
Animals.append("mouse")
Animals.append("bird")
Animals.append("deer")
Animals.append("whale")
Animals.append("elephant")
Animals.append("kangaroo")
Animals.append("tiger")

def SortDescending():
    ArrayLength = 10
    for x in range(0 ,ArrayLength):
        for Y in range(0, ArrayLength - x - 1):
            if Animals[Y][0] < Animals[Y + 1][0]:
                Temp = Animals[Y]
                Animals[Y] = Animals[Y + 1]
                Animals[Y + 1] = Temp


SortDescending()
for x in range(10):
    print(Animals[x])


# DECLARE Animal : ARRAY[0:9] OF STRING
Animal = [""] * 10
Animal = [
    "horse",
    "lion",
    "rabbit",
    "mouse",
    "bird",
    "deer",
    "whale",
    "elephant",
    "kangaroo",
    "tiger",
]


def SortDescending():
    # DECLARE arraylength : INTEGER
    # DECLARE temp : STRING
    global Animal
    arrayLength = len(Animal)
    for x in range(0, arrayLength):
        for y in range(0, arrayLength - 1):
            if Animal[y][0] < Animal[y + 1][0]:
                temp = Animal[y]
                Animal[y] = Animal[y + 1]
                Animal[y + 1] = temp


# print(Animal)
SortDescending()
for i in range(len(Animal)):
    print(Animal[i])

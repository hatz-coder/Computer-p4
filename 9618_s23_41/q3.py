Animal = [""] * 20
Colour = [""] * 10
AnimalTopPointer = 0
ColourTopPointer = 0


def PushAnimal(DataToPush):
    global AnimalTopPointer
    if AnimalTopPointer == 20:
        return False
    else:
        Animal[AnimalTopPointer] = DataToPush
        print(AnimalTopPointer)
        AnimalTopPointer += 1
        return True


def PushColour(DataToPush):
    global ColourTopPointer
    if ColourTopPointer == 10:
        return False
    else:
        Colour[ColourTopPointer] = DataToPush
        ColourTopPointer += 1
        return True


def Readdata():
    global Animal
    global Colour
    try:
        File = open("AnimalData.txt", "r")
        for i in range(8):
            PushAnimal(File.readline().strip())
    except:
        print("No such file exists")
    try:
        File = open("ColourData.txt", "r")
        for i in range(len(Colour)):
            PushColour(File.readline().strip())
    except:
        print("No such file exists")


def PopAnimal():
    global AnimalTopPointer
    if AnimalTopPointer == 0:
        return -1
    else:
        ReturnData1 = Animal[AnimalTopPointer - 1]
        AnimalTopPointer -= 1
        return ReturnData1


def PopColour():
    global ColourTopPointer
    if ColourTopPointer == 0:
        return -1
    else:
        ReturnData = Colour[ColourTopPointer - 1]
        ColourTopPointer -= 1
        return ReturnData


def OutputItem():
    Ani = PopAnimal()
    Col = PopColour()
    if Ani == -1:
        PushColour(Col)
        print("No animal")
    elif Col == -1:
        PushAnimal(Ani)
        print("No colour")
    else:
        print(Col + " " + Ani)


Readdata()
OutputItem()
OutputItem()
OutputItem()
OutputItem()

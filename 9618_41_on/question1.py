DataArray = [" "] * 100


def ReadFile():
    global DataArray
    try:

        File = open("IntegerData.txt", "r")
        for x in range(len(DataArray)):
            DataArray[x] = int(File.readline().strip())
        File.close()
    except IOError:
        print("Couldn't find the file")


def FindValues():
    global DataArray
    timesfound = 0
    number = int(input("Enter the number to be searched: "))
    if number >= 1 and number <= 100:
        for x in range(100):
            # print(DataArray[x])
            if DataArray[x] == number:
                print("Found")
                timesfound += 1
    else:
        print("The number is not within range.")
    print(timesfound)
    return timesfound


def BubbleSort():
    global DataArray
    for x in range(len(DataArray)):
        for y in range(len(DataArray) - 1):
            if DataArray[y] > DataArray[y + 1]:
                temp = DataArray[y + 1]
                DataArray[y + 1] = DataArray[y]
                DataArray[y] = temp


ReadFile()
FindValues()
print(DataArray)
BubbleSort()
print(DataArray)

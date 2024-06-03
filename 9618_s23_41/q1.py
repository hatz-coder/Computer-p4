DataArray = [0] * 25
AFile = open("Data.txt", "r")
for i in range(len(DataArray)):
    DataArray[i] = int(File.readline().strip())
File.close()


def PrintArray(Array):
    line = ""
    for i in range(len(Array)):
        line = line + str(Array[i]) + " "

    print(line)


PrintArray(DataArray)


def LinearSearch(Array, searchItem):
    itemfound = False
    timesfound = 0
    for i in range(len(Array)):
        if Array[i] == searchItem:
            itemfound = True
            timesfound += 1
    return timesfound


searchvalue = -1
while searchvalue < 0 or searchvalue > 100:
    searchvalue = int(input("Enter a number to be searched = "))
print(
    "The number "
    + str(searchvalue)
    + " is found "
    + str(LinearSearch(DataArray, searchvalue))
    + " times."
)

arrayData = [10, 5, 6, 7, 1, 12, 13, 15, 21, 8]


def LinearSearch(searchparam):
    global arrayData
    for x in range(len(arrayData)):
        if arrayData[x] == int(searchparam):
            return True
        else:
            return False


status = LinearSearch(input("Enter the number to be searched: "))
if status == True:
    print("The value was found")
else:
    print("The value couldn't be found")


def BubbleSort():
    global arrayData
    for x in range(len(arrayData)):
        for y in range(len(arrayData) - 1):
            if arrayData[y] > arrayData[y + 1]:
                temp = arrayData[y]
                arrayData[y] = arrayData[y + 1]
                arrayData[y + 1] = temp


print(arrayData)
BubbleSort()
print(arrayData)

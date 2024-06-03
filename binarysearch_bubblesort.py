# BUBBLE SORT ALGORITHM
Thisarray = [10, 3, 2, 4, 5, 6, 68, 25, 21, 85, 52, 94, 12, 56, 32, 16, 90]


def BubbleSort():
    for x in range(len(Thisarray)):
        swapped = False
        for i in range(len(Thisarray) - 1):
            if Thisarray[i] > Thisarray[i + 1]:
                temp = Thisarray[i]
                Thisarray[i] = Thisarray[i + 1]
                Thisarray[i + 1] = temp
                swapped = True
        if not swapped: # If the list is already sorted, then break the loop
            break
    return Thisarray


def BinarySearch():
    searchTerm = int(input("Enter the number to be searched: "))
    found = False
    lb = 0
    ub = len(Thisarray)
    NotinList = False
    while found == False and NotinList == False:
        mp = int((lb + ub) / 2)
        # print(mp)
        print(Thisarray[mp])
        if Thisarray[mp] == searchTerm:
            found = True
        else:
            if Thisarray[mp] > searchTerm:
                ub = mp - 1

            else:
                lb = mp + 1
        if lb > ub:
            NotinList = True
    return found


print(BubbleSort())
print(BinarySearch())

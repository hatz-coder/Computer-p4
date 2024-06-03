Thisarray = [10, 3, 2, 4, 5, 6, 68, 25, 21, 85, 52, 94, 12, 56, 32, 16, 90]


def LinearSearch():
    found = False
    searchterm = int(input("Enter the number to be searched: "))
    for x in range(len(Thisarray)):
        if Thisarray[x] == searchterm:
            found = True
        else:
            found = False
    return "The number is in list: ", found


print(LinearSearch())

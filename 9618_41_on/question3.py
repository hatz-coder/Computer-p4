ArrayNodes = [[-1] * 3 for i in range(20)]
# print(ArrayNodes)
# print(ArrayNodes[0][2])
FreeNode = 6
RootPointer = 0
ArrayNodes[0][0], ArrayNodes[0][1], ArrayNodes[0][2] = 1, 20, 5
ArrayNodes[1][0], ArrayNodes[1][1], ArrayNodes[1][2] = 2, 15, -1
ArrayNodes[2][0], ArrayNodes[2][1], ArrayNodes[2][2] = -1, 3, 3
ArrayNodes[3][0], ArrayNodes[3][1], ArrayNodes[3][2] = -1, 9, 4
ArrayNodes[4][0], ArrayNodes[4][1], ArrayNodes[4][2] = -1, 10, -1
ArrayNodes[5][0], ArrayNodes[5][1], ArrayNodes[5][2] = -1, 58, -1


def SearchValue(Root, Valuetofind):

    global ArrayNodes
    if Root == -1:
        return -1
    else:
        if ArrayNodes[Root][1] == Valuetofind:
            return Root
        else:
            if ArrayNodes[Root][1] == -1:
                return -1
    if ArrayNodes[Root][1] > Valuetofind:
        return SearchValue(ArrayNodes[Root][0], Valuetofind)
    if ArrayNodes[Root][1] < Valuetofind:
        return SearchValue(ArrayNodes[Root][2], Valuetofind)


print(ArrayNodes)


def PostOrder(RootNode):
    if RootNode[0] != -1:
        PostOrder(ArrayNodes[RootNode[0]])
    if RootNode[2] != -1:
        PostOrder(ArrayNodes[RootNode[2]])
    print(RootNode[1])


if SearchValue(RootPointer, 15) == -1:
    print("The value was not found")
else:
    print("The value was found at index", SearchValue(RootPointer, 15))
PostOrder(ArrayNodes[0])

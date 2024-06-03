class Node:
    def __init__(self, data1, nextNode1):
        self.__data = data1
        self.__NextNode = nextNode1

    def GetData(self):
        return self.__data

    def GetNode(self):
        return self.__NextNode

    def UpdateData(self, Data):
        self.__data = Data
        return self.__data

    def UpdateNode(self, NextNode):
        self.__NextNode = NextNode
        return self.__NextNode


startPointer = 0
EmptyList = 5
LinkedList = []
LinkedList.append(Node(1, 1))
LinkedList.append(Node(5, 4))
LinkedList.append(Node(6, 7))
LinkedList.append(Node(7, -1))
LinkedList.append(Node(2, 2))
LinkedList.append(Node(0, 6))
LinkedList.append(Node(0, 8))
LinkedList.append(Node(56, 3))
LinkedList.append(Node(0, 9))
LinkedList.append(Node(0, -1))


def OutputNode(array, startPointer):
    if startPointer == -1:
        return -1
    else:
        print(array[startPointer].GetData())
        return OutputNode(array, array[startPointer].GetNode())


def AddNode():
    global LinkedList
    global EmptyList
    numtoadd = int(input("Enter the number to add in linked list: "))
    if EmptyList == -1:
        return True
    else:
        LinkedList[EmptyList].UpdateData(numtoadd)
        LinkedList[3].UpdateNode(5)
        LinkedList[5].UpdateNode(-1)
    if len(LinkedList) > EmptyList:
        EmptyList += 1
        return False
    else:
        EmptyList = -1


OutputNode(LinkedList, startPointer)

if AddNode() == True:
    print("The linked list is full")
else:
    print("The data item has been added")
# print(LinkedList[5].GetData())

OutputNode(LinkedList, startPointer)


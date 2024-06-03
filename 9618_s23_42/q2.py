class SaleData:
    def __init__(self, IDp, QuantityP):
        self.ID = IDp
        self.Quantity = QuantityP


CircularQueue = [SaleData("", -1)] * 5
Head = 0
Tail = 0
NumberOfItems = 0


def Enqueue(Data):
    global CircularQueue
    global Head
    global Tail
    global NumberOfItems
    if NumberOfItems >= len(CircularQueue):
        # print("Queue is Full")
        return -1
    CircularQueue[Tail] = Data
    if Tail >= len(CircularQueue) - 1:
        Tail = 0
    else:
        Tail = Tail + 1

    NumberOfItems = NumberOfItems + 1


def Dequeue():
    global CircularQueue
    global Head
    global Tail
    global NumberOfItems
    if NumberOfItems == 0:
        # print("Queue is Empty")
        return -2
    else:
        value = CircularQueue[Head]
        Head = Head + 1
        if Head > len(CircularQueue) - 1:
            Head = 0
        NumberOfItems = NumberOfItems - 1
    return value


def EnterRecord():
    ID = input("Enter a ID for the sale")
    Quantity = int(input("Enter the quantity of the item"))
    output = Enqueue(SaleData(ID, Quantity))
    if output == -1:
        print("Full")
    else:
        print("Stored")


# Enqueue(SaleData("afav", 1231))
# print(CircularQueue[1].ID)
EnterRecord()
EnterRecord()
EnterRecord()
EnterRecord()
EnterRecord()
EnterRecord()
popped = Dequeue()
if popped == -2:
    print("The queue is empty")
else:
    print(popped.ID)
EnterRecord()
for x in range(len(CircularQueue)):
    print(CircularQueue[x].ID)
    print(CircularQueue[x].Quantity)

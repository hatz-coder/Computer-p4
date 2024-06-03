QueueArray = [""] * 10  # DECLARE QueueArray :[1:10] of ARRAY
HeadPointer = 0  # DECLARE HeadPointer : INTEGER
TailPointer = 0  # DECLARE TailPointer : INTEGER
NumberofItems = 0  # DECLARE NumberofItems : INTEGER


def Enqueue(DataToAdd):
    global TailPointer
    global NumberofItems
    global QueueArray
    global HeadPointer
    if NumberofItems == 10:
        print("Queue is Full")
        return False
    QueueArray[TailPointxxer] = DataToAdd
    if TailPointer >= len(QueueArray)-1:
        TailPointer = 0
    else:
        TailPointer = TailPointer + 1
        print("Successful")
    NumberofItems = NumberofItems + 1
    return True


def Dequeue():
    global TailPointer
    global NumberofItems
    global QueueArray
    global HeadPointer
    if NumberofItems == 0:
        return False
    temp = QueueArray[HeadPointer]
    QueueArray[HeadPointer] = ""
    if HeadPointer >= 9:
        HeadPointer = 0
    else:
        HeadPointer = HeadPointer + 1
    NumberofItems = NumberofItems - 1
    print("The item removed is ", temp)
    return True


Enqueue("a")
Enqueue("b")

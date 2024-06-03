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
        print("Not Successful")
        return False
    QueueArray[TailPointer] = DataToAdd
    if TailPointer >= 9:
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
        print("Queue is empty")
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


# Enqueue("a")
# Enqueue("b")
# Enqueue("c")
# Enqueue("d")
# Enqueue("e")
# Enqueue("f")
# Enqueue("g")
# Enqueue("h")
# Enqueue("i")
# Enqueue("j")
# Enqueue("k")
Enqueue("Hadi")
Enqueue("Hedi")
Enqueue("Haydeez")
Enqueue("Munchkin")
Enqueue("Pookie")
Enqueue("Huraira")
Enqueue("Hufirira")
Enqueue("Aka")
Enqueue("HoErIa")
Enqueue("Empire")
Enqueue("Gaming")
Dequeue()
Dequeue()
print(QueueArray)

StackData = ["."] * 10  # DECLARE StackData : ARRAY OF INTEGER
StackPointer = 0


def OutputStack():
    for x in range(len(StackData)):
        print(StackData[x])
    print("The value of StackPointer is", StackPointer)


def Push(value):
    global StackPointer
    global StackData
    if StackPointer == -1:
        print("Stack is Full")
        return False
    else:
        StackData[StackPointer] = value
        if StackPointer == len(StackData) - 1:
            StackPointer = -1
        else:
            StackPointer += 1
        print("successful")
        return True


def Pop():
    global StackData
    global StackPointer
    if StackPointer == 0:

        return -1
    else:
        StackPointer -= 1
        temp = StackData[StackPointer]
        StackData[StackPointer] = "."
        print("Successfully Removed", temp)


Push(input("Enter the value to add in stack"))
Push(input("Enter the value to add in stack"))
Push(input("Enter the value to add in stack"))
Push(input("Enter the value to add in stack"))
Push(input("Enter the value to add in stack"))
Push(input("Enter the value to add in stack"))
Push(input("Enter the value to add in stack"))
Push(input("Enter the value to add in stack"))
Push(input("Enter the value to add in stack"))
Push(input("Enter the value to add in stack"))
Push(input("Enter the value to add in stack"))
OutputStack()
Pop()
Pop()
OutputStack()
# print(Push(input("Enter the value to add in stack")))
# print(Push(input("Enter the value to add in stack")))
# print(Push(input("Enter the value to add in stack")))
# print(Push(input("Enter the value to add in stack")))
# print(Push(input("Enter the value to add in stack")))
# print(Push(input("Enter the value to add in stack")))
# print(Push(input("Enter the value to add in stack")))
# print(Push(input("Enter the value to add in stack")))

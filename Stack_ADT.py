# LIFO( Last In, First Out ) MECHANISM - Uses 1 pointer (Stack Pointer)
# Two main functions (Push and Pop)

# import random  # for generating random numbers

# stack = [0] * 10  # array of 10 elements
# stackPointer = 0  # stackPointer


# def append(item):  # function to add an item to the stack
#     global stackPointer
#     global stack
#     if stackPointer < len(stack):  # if the stack is not full
#         stack[stackPointer] = item  # add the item to the stack
#         stackPointer = stackPointer + 1  # increment the stackPointer
#         print(stackPointer)  # print the stackPointer
#     else:
#         print("Stack is full")  # if the stack is full, print "Stack is full"


# for i in range(len(stack) + 2):  # 10 + 2 = 12
#     append(random.randint(1, 100))
#     print(stack)


# ANOTHER TRY

import random

stack = [0] * 10
stackPointer = 0


def Push(item):
    global stack
    global stackPointer
    if stackPointer == len(stack):
        print("Stack is full")
    else:
        stack[stackPointer] = item
        stackPointer += 1
        # print(stackPointer)


def Pop():
    global stack
    global stackPointer
    if stackPointer == 0:
        print("The stack is empty")
    else:
        stackPointer -= 1
        stack[stackPointer] = 0


for i in range(0, len(stack)):
    Push(random.randint(1, 100))
    # print(stack)

# Pop()
# Pop()
print(stack)

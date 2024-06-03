RandomArray = [["."] * 10 for x in range(0, 10)]
import random

print(RandomArray)

for x in range(0, 10):
    for y in range(0, 10):
        RandomArray[x][y] = random.randint(1, 100)


def BubbleSort():
    global RandomArray
    ArrayLength = len(RandomArray) + 1
    for x in range(0, ArrayLength - 1):
        for y in range(0, ArrayLength - 2):
            for z in range(0, ArrayLength - y - 2):
                if RandomArray[x][z] > RandomArray[x][z + 1]:
                    temp = RandomArray[x][z]
                    RandomArray[x][z] = RandomArray[x][z + 1]
                    RandomArray[x][z + 1] = temp


print(RandomArray)
BubbleSort()
print("")
for x in range(0, 10):
    print(RandomArray[x])


def BinarySearch(SearchArray, Lower, Upper, SearchValue):
    if Upper >= Lower:
        Mid = (Lower + (Upper - 1)) // 2
        if SearchArray[0][Mid] == SearchValue:
            print("Found")
            return Mid

        else:
            if SearchArray[0][Mid] > SearchValue:
                return BinarySearch(SearchArray, Lower, Mid - 1, SearchValue)
            else:
                return BinarySearch(SearchArray, Mid + 1, Upper, SearchValue)
    return -1


# print(RandomArray[0][1])
print(BinarySearch(RandomArray, 0, 10, 10))

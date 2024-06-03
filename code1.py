TheData = [20,3,4,8,12,99,4,26,4]
def InsertionSort(TheData):
    for count in range(1,len(TheData)):
        DatatoInsert = TheData[count]
        Inserted = 0 
        NextValue = count-1
        while NextValue>= 0 and Inserted!=1:
            if DatatoInsert < TheData[NextValue]:
                TheData[NextValue+1] = TheData[NextValue]
                NextValue = NextValue-1
                TheData[NextValue+1] = DatatoInsert
            else:
                Inserted=1
def Display (TheData):
    for x in range(len(TheData)):
        print(TheData[x],end="|")
    print()
print("The array before Sorting")
print(TheData)
InsertionSort(TheData)
print("The array after Sorting")
print(TheData)

def Find():
    items = int(input("enter item to be searched : "))
    found = False
    index =0 
    while found == False and index<= len(TheData)-1:
        if items == TheData[index]:
            found= True
        else:
            index = index+1
    if found==False:
        print("Not Found !")
        return False
    else:
        print("Found at index =",index)
        return True

Find()
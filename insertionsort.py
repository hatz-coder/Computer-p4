def insertion_sort(arr):  # A function to sort an array using insertion sort
    # for i in range(1, len(arr)): # Loop through the array
    #     key = arr[i] # The current element we are sorting
    #     j = i - 1 # A variable to keep track of the index of the previous element
    #     while j >= 0 and key < arr[j]: # If the current element is less than the previous element
    #         arr[j + 1] = arr[j] # Move the previous element to the next position
    #         j -= 1 # Move to the next previous element
    #     arr[j + 1] = key # Move the current element to the next position
    # return arr # Return the sorted array

    # for i in range(1, len(arr)):
    #     valuetoinsert = arr[i] # The current element we are sorting
    #     previousindex = i - 1 # A variable to keep track of the index of the previous element
    #     while (previousindex >= 0) and (arr[previousindex] > valuetoinsert): # If the current element is less than the previous element
    #         arr[previousindex + 1] = arr[previousindex] # Move the previous element to the next position
    #         previousindex = previousindex - 1 # Move to the next previous element
    #     arr[previousindex + 1] = valuetoinsert # Move the current element to the next position
    # return arr

    # for i in range(1, len(arr)):
    #     valuetoinsert = arr[i]
    #     previousindex = i - 1
    #     while (previousindex >= 0) and (arr[previousindex] > valuetoinsert):
    #         arr[previousindex + 1] = arr[previousindex]
    #         previousindex = previousindex - 1
    #     arr[previousindex + 1] = valuetoinsert
    # return arr

    for i in range(1, len(arr)):
        temp = arr[i]
        holeposition = i
        while (holeposition > 0) and (arr[holeposition - 1] > temp):
            arr[holeposition] = arr[holeposition - 1]
            holeposition = holeposition - 1
        arr[holeposition] = temp
    return arr


# Test the function
print(insertion_sort([4, 3, 2, 10, 12, 1, 5, 6]))

arr = [5, 22, 29, 39, 19, 51, 78, 96, 84]
i = 1

# 'i' is initially set to 1, so that the first comparison is: element 1 < element 0
# additional variable 'j' is needed (in the event of a swap) to loop back from the point of 'i' to the beginning of the array, 
# in case the element just swapped is smaller than any earlier array elements. The newly swapped element will be checked against
# all previous elements and will continue to be swapped until it is not less than an earlier element, or until it has been 
# moved to element 0
while (i < len(arr)):  
    j = i
    while (j > 0) and (arr[j] < arr[j-1]): 
            
        temp = arr[j]
        arr[j] = arr [j-1]
        arr[j-1] = temp
        j -= 1              # j decrements by 1 until the while condition fails (it reaches 0 or arr[j] > arr [j-1])
    i += 1                  # i increments by 1 until it is no longer less than the length of the array


print(arr)


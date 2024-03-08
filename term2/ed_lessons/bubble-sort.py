def bubbleSort(lst):
    unsortedEnd = len(lst)-1 # variable that represents the end of the unsorted region of the list
    iterations = 0
    while unsortedEnd > 0:
        
        for i in range(0, unsortedEnd): # traverse the list from 0 to the end if the unsorted region of the list
            if lst[i] > lst[i+1]: # if the current element is larger than the next element, then swap them
                tmp = lst[i+1]
                lst[i+1] = lst[i]
                lst[i] = tmp
        unsortedEnd -= 1
        iterations += 1
        print(f'iteration: {iterations}')

#Driver code

bubbleList = [i for i in range(99, 0, -1)]
bubbleList = [6, 55, 77, 2, 44, 28, 39, 102, 152, 83, 21, 62, 80]
# bubbleList = [55, 77, 100, 44, 2, 80]
bubbleList = [100, 80, 77, 55, 44, 2]
bubbleList = [77, 2, 80, 55, 100, 44]

l1 = [24, 8]
l2 = [50, 40, 25, 12]
l3 = [140, 115, 100, 80, 77, 55, 44, 2]
l4 = [293, 258, 227, 221, 207, 190, 160, 145, 140, 115, 100, 80, 77, 55, 44, 2]

bubbleSort(bubbleList)
print(bubbleList)
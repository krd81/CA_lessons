def mergeSort(lst, iterations):      
      if len(lst) > 1:
        print(lst)
        print(len(lst))
        # Split part of the algorithm
        middle = len(lst) // 2 # floor division to find middle of the list
        leftList = lst[:middle]
        rightList = lst[middle:]
        
        # print(f'mergeSort(left) called')
        mergeSort(leftList, iterations) # left side of the list
        print('-')
        # print(f'mergeSort(left) exit')
        
        # print(f'mergeSort(right) called')
        mergeSort(rightList, iterations) # right side of the list
        print('-')
        # print(f'mergeSort(right) exit')

        leftIndex = rightIndex = mergedIndex = 0

        # merge part of the algorithm
        while leftIndex < len(leftList) and rightIndex < len(rightList):
          if leftList[leftIndex] < rightList[rightIndex]:
            lst[mergedIndex] = leftList[leftIndex]
            leftIndex += 1
            iterations +=1
            print('<<<iteration>>>')
          else:
            lst[mergedIndex] = rightList[rightIndex]
            rightIndex += 1
            iterations +=1
            print('<<<iteration>>>')
          mergedIndex += 1
        # Ensure the remaining elements of either leftList or rightList are appended to the end of lst
        while leftIndex < len(leftList):
          lst[mergedIndex] = leftList[leftIndex]
          leftIndex += 1
          mergedIndex += 1
        while rightIndex < len(rightList):
          lst[mergedIndex] = rightList[rightIndex]
          rightIndex += 1
          mergedIndex += 1
      return iterations

list = [6, 55, 77, 2, 44, 28, 39, 102, 152, 83, 21, 62, 80]
list = [55, 77, 2, 44, 102, 80]
list = [140, 115, 100, 80, 77, 55]
list = [254, 246, 241, 235, 222, 211, 200, 194, 190, 180, 175, 157, 140, 115, 100, 80, 77, 55, 44, 2]
# list = [24, 8]
# list = [39, 24, 8, 3]
list = [254, 246, 241, 235, 222, 211, 200, 194, 190, 180, 175, 157, 140, 115, 100, 80]

def count_iterations():
   iterations += 1
   return iterations

# print(f'mergeSort(main) called')
complexity = mergeSort(list, 0)
# print(f'mergeSort(main) exit')

print(list)
# print(f'Iterations is {complexity}')
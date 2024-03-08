def mergeSort(self, lst):
      if len(lst) > 1:
        # Split part of the algorithm
        middle = len(lst) // 2 # floor division to find middle of the list
        leftList = lst[:middle]
        rightList = lst[middle:]
        self.mergeSort(leftList) # left side of the list
        self.mergeSort(rightList) # right side of the list

        leftIndex = rightIndex = mergedIndex = 0

        # merge part of the algorithm
        while leftIndex < len(leftList) and rightIndex < len(rightList):
          if leftList[leftIndex] < rightList[rightIndex]:
            lst[mergedIndex] = leftList[leftIndex]
            leftIndex += 1
          else:
            lst[mergedIndex] = rightList[rightIndex]
            rightIndex += 1
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

list = [6, 55, 77, 2, 44, 28, 39, 102, 152, 83, 21, 62, 80]

mergeSort(list)

print(list)
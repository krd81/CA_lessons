arr = [5, 22, 29, 39, 19, 51, 78, 96, 84]
i = 0

while (i<len(arr)) and (arr[i] < arr[i+1]):
    i += 1
    print(i)

temp = arr[i]
arr[i] = arr [i+1]
arr[i+1] = temp
    
print(arr)

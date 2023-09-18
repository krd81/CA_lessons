
arr = [5, 22, 33, 44, 55, 29 ,66, 77, 16]
i = 0

while (i < arr.len() -1) and (arr[i] < arr[i+1]):
    i+= i
    print(i)
    arr[i] = arr[i+1]
    arr[i+1] = arr[i]

print(arr)

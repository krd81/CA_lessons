arr = [5, 22, 29, 39, 19, 51, 78, 96, 84]
i = 0
j = 0

while (i<8) and (arr[i] < arr[i+1]):
    i += i
print(i)
j = arr[i]
arr[i] = arr [i+1]
arr[i+1] = j 




# Python Program for recursive binary search. 
  
# Returns index of x in arr if present, else -1 
def binarySearch (arr, l, r, x): 
    
    
    # Check base case 
    if r >= l: 
  
        mid = (l + (r - l)//2)
        print("<<<Array divided>>>")
  
        # If element is present at the middle itself 
        if arr[mid] == x: 
            return mid 
          
        # If element is smaller than mid, then it  
        # can only be present in left subarray 
        elif arr[mid] > x: 
            return binarySearch(arr, l, mid-1, x) 
  
        # Else the element can only be present  
        # in right subarray 
        else: 
            return binarySearch(arr, mid + 1, r, x) 
  
    else: 
        # Element is not present in the array 
        return -1
  
# Test array 
# arr = [ 2, 3, 4] 
# arr = [ 2, 3, 4, 10] 
# arr = [ 2, 3, 4, 10, 40] 
# arr = [ 2, 3, 4, 10, 40, 45] 
# arr = [ 2, 3, 4, 10, 40, 45, 50] 
# arr = [ 2, 3, 4, 10, 40, 45, 50, 55] 
# arr = [ 2, 3, 4, 10, 40, 45, 50, 55, 60] 
# arr = [ 2, 3, 4, 10, 40, 45, 50, 55, 60, 65] 
# arr = [ 2, 3, 4, 10, 40, 45, 50, 55, 60, 65, 70] 
# arr = [ 2, 3, 4, 10, 40, 45, 50, 55, 60, 65, 70, 75] 
# arr = [ 2, 3, 4, 10, 40, 45, 50, 55, 60, 65, 70, 75, 80] 
# arr = [ 2, 3, 4, 10, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85] 
# arr = [ 2, 3, 4, 10, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90] 
arr = [ 2, 3, 4, 10, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95] 
# arr = [ 2, 3, 4, 10, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100] 
# arr = [ 2, 3, 4, 10, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100, 105] 
# arr = [ 2, 3, 4, 10, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100, 105, 110] 
# arr = [ 2, 3, 4, 10, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100, 105, 110, 115] 



print(arr)
print(f"Array length is {len(arr)}")
  
# Function call 
for i in arr:
    result = binarySearch(arr, 0, len(arr)-1, i) 


    if result != -1: 
        print (f"Element {i} is present at index {result}")
    else: 
        print ("Element is not present in array")
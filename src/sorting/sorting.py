def merge(leftArray, rightArray):
    
    merged_arr = []

    leftIndex, rightIndex = 0, 0

    while leftIndex < len(leftArray) and rightIndex < len(rightArray):
        if leftArray[leftIndex] < rightArray[rightIndex]:
            merged_arr.append(leftArray[leftIndex])
            leftIndex += 1
        else:
            merged_arr.append(rightArray[rightIndex])
            rightIndex += 1
            
    merged_arr += leftArray[leftIndex:]
    merged_arr += rightArray[rightIndex:]

    return merged_arr

def merge_sort(arr):
    #guard for empty arr
    if len(arr) <= 1:
        return arr
 
    midIndex = int(len(arr) / 2)
      
    leftArray = merge_sort(arr[:midIndex])
    rightArray = merge_sort(arr[midIndex:])

    return merge(leftArray, rightArray)
    
# STRETCH: implement the recursive logic for merge sort in a way that doesn't 
# utilize any extra memory
# In other words, your implementation should not allocate any additional lists 
# or data structures; it can only re-use the memory it was given as input
#def merge_in_place(arr, start, mid, end):
#    # Your code here
#
#
#def merge_sort_in_place(arr, l, r):
#    # Your code here


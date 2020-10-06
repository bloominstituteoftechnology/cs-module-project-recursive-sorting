# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(left, right):
    elements = len(left) + len(right)
    merged_arr = [0] * elements # why not just merged_arr = []

    # Your code here
    i = j = k = 0
        
    # Copy data to temp arrays L[] and R[]
    while i < len(left) and j < len(right): 
        if left[i] < right[j]: 
            merged_arr[k] = left[i] 
            i+= 1
        else: 
            merged_arr[k] = right[j] 
            j+= 1
        k+= 1
        
    # Checking if any element was left 
    while i < len(left): 
        merged_arr[k] = left[i] 
        i+= 1
        k+= 1
    while j < len(right): 
        merged_arr[k] = right[j] 
        j+= 1
        k+= 1

    return merged_arr
  
  
# TO-DO: implement the Merge Sort function below recursively
def merge_sort(arr):
    if len(arr) >1:
        mid = len(arr)//2 # Finding the mid of the array 
        L = arr[:mid] # Dividing the array elements  
        R = arr[mid:] # into 2 halves 

        L = merge_sort(L) # Sorting the first half 
        R = merge_sort(R) # Sorting the second half 
        result = merge(L, R)
        return result
    else:
        return arr


        

# STRETCH: implement the recursive logic for merge sort in a way that doesn't 
# utilize any extra memory
# In other words, your implementation should not allocate any additional lists 
# or data structures; it can only re-use the memory it was given as input
# def merge_in_place(arr, start, mid, end):
#     # Your code here


# def merge_sort_in_place(arr, l, r):
#     # Your code here


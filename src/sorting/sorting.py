# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements

    # Your code here
    while (len(arrA)> 0 and len(arrB)> 0):
        if arrA[0] < arrB[0]:
            merged_arr.append(arrA[0])
            arrA.pop(0)
        else:
            merged_arr.append(arrB[0])
            arrB.pop(0)

    return merged_arr

# TO-DO: implement the Merge Sort function below recursively
def merge_sort(arr):
    # Your code here
    if len(arr) >1: 
        mid = len(arr)//2 # Finding the mid of the array 
        LHS = arr[:mid] # Dividing the array elements  
        RHS = arr[mid:] # into 2 halves 
  
        merge_sort(LHS) # Sorting the first half 
        merge_sort(RHS) # Sorting the second half 
  
        i = j = k = 0
          
        # Copy data to temp arrays L[] and R[] 
        while i < len(LHS) and j < len(RHS): 
            if LHS[i] < RHS[j]: 
                arr[k] = LHS[i] 
                i+= 1
            else: 
                arr[k] = RHS[j] 
                j+= 1
            k+= 1
          
        # Checking if any element was left 
        while i < len(LHS): 
            arr[k] = LHS[i] 
            i+= 1
            k+= 1
          
        while j < len(RHS): 
            arr[k] = RHS[j] 
            j+= 1
            k+= 1


    return arr

# STRETCH: implement the recursive logic for merge sort in a way that doesn't 
# utilize any extra memory
# In other words, your implementation should not allocate any additional lists 
# or data structures; it can only re-use the memory it was given as input
#def merge_in_place(arr, start, mid, end):
    # Your code here


#def merge_sort_in_place(arr, l, r):
    # Your code here


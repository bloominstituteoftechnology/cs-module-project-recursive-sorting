# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(lefthalf, righthalf):
    merged_array = lefthalf + righthalf

    i=0
    j=0
    k=0

    while i < len(lefthalf) and j < len(righthalf): # loop if starting index is less than the length of the array
        if lefthalf[i] <= righthalf[j]: # if the left half element at the given index is less than or equal to the right half element at the given index
            merged_array[k]=lefthalf[i] # take the given index in the merged array and set it to the element of the left half given index
            i=i+1 # increase the "position" on the left by 1
        else: # if the left half element at the given index is greater than the right half element at the given index
            merged_array[k]=righthalf[j] # take the given index in the merged array and set it to the element of the right half given index
            j=j+1 # increase the "position" on the right by 1
        k=k+1 # increase the "position" on the merged_array by 1

    while i < len(lefthalf): # loop if starting index is less than the length of the LEFT array
        merged_array[k]=lefthalf[i] # take the given index in the merged array and set it to the element of the left half given index
        i=i+1 # increase the "position" on the left by 1
        k=k+1 # increase the "position" on the merged_array by 1

    while j < len(righthalf): # loop if starting index is less than the length of the RIGHT array
        merged_array[k]=righthalf[j] # take the given index in the merged array and set it to the element of the right half given index
        j=j+1 # increase the "position" on the right by 1
        k=k+1 # increase the "position" on the merged_array by 1
    
    print(f"merged array: {merged_array}")
    return merged_array

# TO-DO: implement the Merge Sort function below recursively
def merge_sort(arr):
    if len(arr) > 1: # make sure we have elements in our list
        mid = len(arr) // 2 # grab the mid point by taking the length and diving by 2
        left = arr[:mid] # declare a left side array (all the elements up to the mid point)
        right = arr[mid:] # declare a right side array (all the elements from the mid point and beyond)

        if len(left) > 1:
            left = merge_sort(left) # recursively call merge_sort() on LHS
        if len(right) > 1:
            right = merge_sort(right) # recursively call merge_sort() on RHS
        
        arr = merge(left, right) # merge sorted pieces
    print(f"arr: {arr}")
    return arr

merge_sort([54,26,93,17,77,31,44,55,20])
# STRETCH: implement the recursive logic for merge sort in a way that doesn't utilize any extra memory
# In other words, your implementation should not allocate any additional lists 
# or data structures; it can only re-use the memory it was given as input
# def merge_in_place(arr, start, mid, end):
#     # Your code here


# def merge_sort_in_place(arr, l, r):
#     # Your code here


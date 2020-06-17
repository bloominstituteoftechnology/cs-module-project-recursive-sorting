# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements

    # Your code here
    # set indices
    a = 0
    b = 0
    # loop through all
    for i in range(elements):
        # if a is out of range
        if a >= len(arrA):
            # add to merged_arr
            merged_arr[i] = arrB[b]
            # increase index
            b += 1
        # if b is out of range
        elif b >= len(arrB):
            # add to merged_arr
            merged_arr[i] = arrA[a]
            # increase index
            a += 1
        # if a is smaller
        elif arrA[a] < arrB[b]:
            # add to merged_arr
            merged_arr[i] = arrA[a]
            # increase index
            a += 1
        # if b is smaller
        else:
            # add to merged_arr
            merged_arr[i] = arrB[b]
            # increase index
            b += 1

    return merged_arr

# TO-DO: implement the Merge Sort function below recursively
def merge_sort(arr):
    # Your code here
    # base case: when list gets down to length 1
    if len(arr) > 1:
        # divide array into left and right halves
        left = merge_sort(arr[:len(arr)//2])
        right = merge_sort(arr[len(arr)//2:])
        #merges two arrays
        arr = merge(left,right)

    return arr

# STRETCH: implement the recursive logic for merge sort in a way that doesn't 
# utilize any extra memory
# In other words, your implementation should not allocate any additional lists 
# or data structures; it can only re-use the memory it was given as input
def merge_in_place(arr, start, mid, end):
    # Your code here
    pass


def merge_sort_in_place(arr, l, r):
    # Your code here
    pass


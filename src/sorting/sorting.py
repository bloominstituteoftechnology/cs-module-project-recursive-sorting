# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements

    # Your code here
    a, b = 0,0

    # loop through our merged array
    for item in range(len(merged_arr)):
        if a >= len(arrA):
            merged_arr[item] = arrB[b]
            b += 1
        elif b >= len(arrB):
            merged_arr[item] = arrA[a]
            a += 1
        elif arrA[a] < arrB[b]:
            merged_arr[item] = arrA[a]
            a += 1
        else: 
            merged_arr[item] = arrB[b]
            b += 1

    return merged_arr

    # TO-DO: implement the Merge Sort function below recursively
def merge_sort(arr):
    # Your code here
    if len(arr) > 1:
        left = merge_sort(arr[0:len(arr) // 2])
        right = merge_sort(arr[len(arr) // 2:])
        arr = merge(left, right)
    return arr

# STRETCH: implement the recursive logic for merge sort in a way that doesn't 
# utilize any extra memory
# In other words, your implementation should not allocate any additional lists 
# or data structures; it can only re-use the memory it was given as input
#def merge_in_place(arr, start, mid, end):
    # Your code here


#def merge_sort_in_place(arr, l, r):
    # Your code here


# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB, n1, n2):
    n1 = len(arrA) 
    n2 = len(arrB)
    merged_arr = [None] * (n1 + n2)

    # Your code here
    i = 0
    j = 0
    k = 0

    #traverse both arrays
    while i < n1 and j < n2:
        if arrA[i] < arrB[j]:
            merged_arr[k] = arrA[i]
            k = k + 1
            i = i + 1
        else:
            merged_arr[k] = arrB[j]
            k = k + 1
            j = j + 1
    while i < n1:
        merged_arr[k] = arrA[i]
        k = k + 1
        i = i + 1
    while j < n2:
        merged_arr[k] = arrB[j]
        k = k + 1
        j = j + 1

    return merged_arr

# TO-DO: implement the Merge Sort function below recursively
def merge_sort(arr):
    # Your code here
    pass

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

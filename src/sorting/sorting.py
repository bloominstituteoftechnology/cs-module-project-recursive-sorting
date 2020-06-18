# TO-DO: complete the helper function below to merge 2 sorted arrays


def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements
    i = 0
    j = 0
    k = 0

    while i < len(arrA) and j < len(arrB):
        if arrA[i] < arrB[j]:
            merged_arr[k] = arrA[i]
            k += 1
            i += 1
        else:
            merged_arr[k] = arrB[j]
            k += 1
            j += 1

    while i < len(arrA):
        merged_arr[k] = arrA[i]
        k += 1
        i += 1
    while j < len(arrB):
        merged_arr[k] = arrB[j]
        k += 1
        j += 1
    return merged_arr

# TO-DO: implement the Merge Sort function below recursively
def merge_sort(arr):
    # Your code here
    if len(arr) > 1:
        mid = int(len(arr) / 2)
        L = arr[:mid]
        R = arr[mid:]

        left = merge_sort(L)
        right = merge_sort(R)

        arr = merge(left, right)

    return arr

# STRETCH: implement the recursive logic for merge sort in a way that doesn't
# utilize any extra memory
# In other words, your implementation should not allocate any additional lists 
# or data structures; it can only re-use the memory it was given as input
# def merge_in_place(arr, start, mid, end):
#     # Your code here
#
#
# def merge_sort_in_place(arr, l, r):
#     # Your code here

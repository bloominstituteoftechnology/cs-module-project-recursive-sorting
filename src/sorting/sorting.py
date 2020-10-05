import math
# TO-DO: complete the helper function below to merge 2 sorted arrays


def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = []

    # Your code here
    while elements > 0:
        if len(arrA) > 0 and len(arrB) > 0:
            if arrA[0] < arrB[0]:
                merged_arr.append(arrA.pop(0))
            else:
                merged_arr.append(arrB.pop(0))
        elif len(arrA) == 0:
            while len(arrB) > 0:
                merged_arr.append(arrB.pop(0))
        elif len(arrB) == 0:
            while len(arrA) > 0:
                merged_arr.append(arrA.pop(0))
        elements -= 1

    return merged_arr

# TO-DO: implement the Merge Sort function below recursively


def merge_sort(arr):
    # Your code here
    middle = math.floor(len(arr)/2)

    left_arr = arr[:middle]
    right_arr = arr[middle:]

    if len(left_arr) > 1:
        left_arr = merge_sort(left_arr)
    if len(right_arr) > 1:
        right_arr = merge_sort(right_arr)

    arr = merge(left_arr, right_arr)

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

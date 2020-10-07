# TO-DO: complete the helper function below to merge 2 sorted arrays
# def merge(arrA, arrB):
#     elements = len(arrA) + len(arrB)
#     merged_arr = [0] * elements

#     # Your code here


#     return merged_arr


def merge(arrA, arrB):
    """Merge sort merging function."""

    arrA_index, arrB_index = 0, 0
    result = []
    while arrA_index < len(arrA) and arrB_index < len(arrB):
        if arrA[arrA_index] < arrB[arrB_index]:
            result.append(arrA[arrA_index])
            arrA_index += 1
        else:
            result.append(arrB[arrB_index])
            arrB_index += 1

    result += arrA[arrA_index:]
    result += arrB[arrB_index:]
    return result

# TO-DO: implement the Merge Sort function below recursively
def merge_sort(arr):
    """Merge sort algorithm implementation."""

    if len(arr) <= 1:  # base case
        return arr

    # divide arr in half and merge sort recursively
    half = len(arr) // 2
    left = merge_sort(arr[:half])
    right = merge_sort(arr[half:])

    return merge(left, right)

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

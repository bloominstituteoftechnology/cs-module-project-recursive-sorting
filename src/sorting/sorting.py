# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements

    current_index = 0
    arrA_index = 0
    arrB_index = 0

    while current_index < elements:
        if arrB_index < len(arrB) and arrA_index < len(arrA):
            if arrA[arrA_index] > arrB[arrB_index]:
                merged_arr[current_index] = arrB[arrB_index]
                arrB_index += 1

            else:
                merged_arr[current_index] = arrA[arrA_index]
                arrA_index += 1

        elif arrB_index < len(arrB):
            merged_arr[current_index] = arrB[arrB_index]
            arrB_index += 1
        else:
            merged_arr[current_index] = arrA[arrA_index]
            arrA_index += 1

        current_index += 1

    return merged_arr

# TO-DO: implement the Merge Sort function below recursively

# Divide and conquer strategy


def merge_sort(arr):

    if len(arr) > 1:
        midpoint = len(arr) // 2  # Integer division

        left = arr[:midpoint]

        right = arr[midpoint:]

        return merge(merge_sort(left), merge_sort(right))  # Recursion

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

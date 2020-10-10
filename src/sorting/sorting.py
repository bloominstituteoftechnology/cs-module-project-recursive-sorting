# TO-DO: complete the helper function below to merge 2 sorted arrays
# from searching import searching

def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements
    pointer_a = 0
    pointer_b = 0

    # Your code here
    # if len(arrA) == 0:
    #     merged_a.append(arrB)     #-needed to put in merged_arr
    # elif len(arrB) == 0:
    #     merged_b.append(arrA)

    # else:
    #     for i in arrA:
    #         for j in arrB:
    #             if i < j:
    #                 merged_arr.append(i)

    # return merged_arr

    for i in range(0, elements):
        if pointer_a >= len(arrA):
            merged_arr[i] = arrB[pointer_b]
            pointer_b += 1

        elif pointer_b >= len(arrB):
            merged_arr[i] = arrA[pointer_a]
            pointer_a += 1

        elif arrA[pointer_a] < arrB[pointer_b]:
            merged_arr[i] = arrA[pointer_a]
            pointer_a += 1

        else:
            merged_arr[i] = arrB[pointer_b]
            pointer_b += 1

    return merged_arr

# TO-DO: implement the Merge Sort function below recursively
def merge_sort(arr):
    # Your code here
    if len(arr) > 1:
        left = merge_sort(arr[0: len(arr) // 2])
        right = merge_sort(arr[len(arr) // 2:])

        arr = merge(left, right)

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


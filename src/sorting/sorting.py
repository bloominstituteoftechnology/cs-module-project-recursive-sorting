# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    # elements = len(arrA) + len(arrB)
    # merged_arr = [0] * elements

    # yo that stuff wasnt needed whats wrong with you

    # Your code here
    i = j = 0
    merged = []

    while i < len(arrA) and j < len(arrB):
        if arrA[i] <= arrB[j]:
            merged.append(arrA[i])
            i += 1
        else:
            merged.append(arrB[j])
            j += 1

    merged += arrA[i:]
    merged += arrB[j:]
    return merged


# TO-DO: implement the Merge Sort function below recursively
def merge_sort(arr):
    # Your code here
    if (n := len(arr)) <= 1:
        return arr
    else:
        m = n//2

        arrA = merge_sort(arr[:m])
        arrB = merge_sort(arr[m:])

        return merge(arrA, arrB)

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

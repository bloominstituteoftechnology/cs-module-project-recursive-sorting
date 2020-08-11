# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements

    for i in range(elements):
        # check for empty arrays and had remainder of second
        if not arrA:
            for indx in range(len(arrB)):
                merged_arr[i] = arrB[indx]
                i += 1
            break
        if not arrB:
            for indx in range(len(arrA)):
                merged_arr[i] = arrA[indx]
                i += 1
            break

        if arrA[0] <= arrB[0]:
            merged_arr[i] = arrA.pop(0)
        else:
            merged_arr[i] = arrB.pop(0)
        
    return merged_arr

# TO-DO: implement the Merge Sort function below recursively
def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    middle = len(arr) // 2
    arrL = merge_sort(arr[:middle])
    arrR = merge_sort(arr[middle:])

    arr = merge(arrL,arrR)

    return arr

# STRETCH: implement the recursive logic for merge sort in a way that doesn't 
# utilize any extra memory
# In other words, your implementation should not allocate any additional lists 
# or data structures; it can only re-use the memory it was given as input
# def merge_in_place(arr, start, mid, end):
#     # Your code here


# def merge_sort_in_place(arr, l, r):
#     # Your code here


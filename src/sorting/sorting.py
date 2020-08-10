# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    lenA = len(arrA)
    lenB = len(arrB)
    merged_arr = [0] * (lenA + lenB)

    indexA = 0
    indexB = 0

    while indexA < (lenA - 1) or indexB < (lenB - 1):
        if indexA == lenA - 1:
            while indexB < lenB - 1:
                merged_arr[lenA + indexB] = arrB[indexB]
                indexB += 1
            return merged_arr.extend(arrB[indexB:])
        elif indexB == lenB - 1:
            while indexA < lenA - 1:
                merged_arr[lenB + indexA] = arrA[indexA]
                indexA += 1
            return merged_arr.extend(arrB[indexB:])
        else:
            if arrA[indexA] <= arrB[indexB]:
                merged_arr[indexA + indexB] = arrA[indexA]
                indexA += 1
            else:
                merged_arr[indexA + indexB] = arrB[indexB]
                indexB += 1

    return merged_arr

# TO-DO: implement the Merge Sort function below recursively
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    
    middle = len(arr) // 2
    return merge(merge_sort(arr[:middle - 1]), merge_sort(arr[middle:]))

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


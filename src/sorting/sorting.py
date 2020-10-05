# TO-DO: complete the helper function below to merge 2 sorted arrays

def merge(arrA, arrB):
    merged_arr = [0] * (len(arrA) + len(arrB))

    j = 0
    k = 0

    while j < len(arrA) or k < len(arrB):
        if j >= len(arrA):
            while k <= len(arrB) - 1:
                merged_arr[len(arrA) + k] = arrB[k]
                k += 1
            return merged_arr
        elif k >= len(arrB):
            while j <= len(arrA) - 1:
                merged_arr[len(arrB) + j] = arrA[j]
                j += 1
            return merged_arr
        else:
            if arrA[j] <= arrB[k]:
                merged_arr[j + k] = arrA[j]
                j += 1
            else:
                merged_arr[j + k] = arrB[k]
                k += 1

    return merged_arr

arrA = [0,1]
arrB = [2,3]
print(merge(arrA, arrB))
# TO-DO: implement the Merge Sort function below recursively
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    
    middle = len(arr) // 2
    return merge(merge_sort(arr[:middle]), merge_sort(arr[middle:]))

arr1  = [2,3,4,5,6,1]
print(merge_sort(arr1))

# STRETCH: implement the recursive logic for merge sort in a way that doesn't 
# utilize any extra memory
# In other words, your implementation should not allocate any additional lists 
# or data structures; it can only re-use the memory it was given as input
def merge_in_place(arr, start, mid, end):
    # Your code here
    pass


def merge_sort_in_place(arr, l, r):
    pass
    # Your code here
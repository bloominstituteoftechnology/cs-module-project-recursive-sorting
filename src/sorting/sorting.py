# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements

    # Your code here
    a = 0
    b = 0
    i = 0

    while a < len(arrA) and b < len(arrB):
        if arrA[a] < arrB[b]:
            merged_arr[i] = arrA[a]
            a += 1
            
        else:
            merged_arr[i] = arrB[b]
            b += 1
        
        i += 1

    if a < len(arrA):
        while a < (len(arrA)):
            merged_arr[i] = arrA[a]
            i += 1
            a += 1

    if b < len(arrB):
        while b < (len(arrB)):
            merged_arr[i] = arrB[b]
            i += 1
            b += 1


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

if __name__ == "__main__":
    arr1 = [1,3,5]
    arr2 = [2,4,6]
    print(merge(arr1,arr2))
    arr3 = [1, 5, 8, 4, 2, 9, 6, 0, 3, 7]
    print(merge_sort(arr3))
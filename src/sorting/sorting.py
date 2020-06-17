# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = []

    # Your code here
    i = 0
    j = 0
    while i < len(arrA) and j < len(arrB):
        if arrA[i] < arrB[j]:
            merged_arr.append(arrA[i])
            i += 1
        else:
            merged_arr.append(arrB[j])
            j += 1
    merged_arr += arrA[i:]
    merged_arr += arrB[j:]
    return merged_arr

# print(merge([4],[1]))

# TO-DO: implement the Merge Sort function below recursively
def merge_sort(arr):
    print('first arr,a and b')
    print(arr)
    # Your code here
    if len(arr) <= 1:
        return arr
        
    mid = round(len(arr)/2)
    arrA = merge_sort(arr[:mid])
    arrB = merge_sort(arr[mid:])

    print('before merge')
    print(arrA)
    print(arrB)
    arr = merge(arrA,arrB)

    print('after merge')

    print(arr)

    return arr

ans = merge_sort([2,41,9,5,100,88])
print('_____________')
print(ans)
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


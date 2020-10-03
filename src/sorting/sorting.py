# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements

    # Your code here
    new_arr = []

    indexA = 0
    indexB = 0

    while (indexA + indexB) < elements:

        if (indexA < len(arrA)) and (indexB < len(arrB)) and (arrA[indexA] < arrB[indexB]):
            new_arr.append(arrA[indexA])
            indexA += 1 
        elif (indexA < len(arrA)) and (indexB < len(arrB)) and (arrA[indexA] < arrB[indexB]):
            new_arr.append(arrB[indexB])
            indexB += 1
        elif indexB < len(arrB):
            new_arr.append(arrB[indexB])
            indexB += 1
        elif indexA < len(arrA):
            new_arr.append(arrA[indexA])
            indexA += 1
            


    return new_arr

# TO-DO: implement the Merge Sort function below recursively
def merge_sort(arr):
    if len(arr) > 1:
        middle = len(arr)//2
        left = arr[:middle]
        right = arr[middle:]
        leftArr = merge_sort(left)
        rightArr = merge_sort(right)

        arr = merge(leftArr, rightArr)

    return arr

# STRETCH: implement the recursive logic for merge sort in a way that doesn't 
# utilize any extra memory
# In other words, your implementation should not allocate any additional lists 
# or data structures; it can only re-use the memory it was given as input
def merge_in_place(arr, start, mid, end):
    # Your code here
    return


def merge_sort_in_place(arr, l, r):
    # Your code here
    return


# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements
    # Your code here
    if not len(arrA) or not len(arrB):
        return arrA or arrB
    combine = []
    i = 0
    j = 0
    while len(combine) < len(elements):
        if arrA[i] < arrB[j]:
            combine.append(arrA[i])
            i += 1
        else:
             combine.append(arrB[j])
             j += 1
        if i == len(arrA) or j == len(arrB):
            combine.extend(arrA[i:] or arrB[j:])
            break
            


    return merged_arr

# TO-DO: implement the Merge Sort function below recursively


def merge_sort(arr):
    # Your code here
    if len(arr) < 2:
        return arr
    
    mid = int((len(arr))/2)  # Finding the mid of the array
    leftArr = merge_sort(arr[:mid])  # Dividing the array arr
    rightArr = merge_sort(arr[mid:])  # into 2 halves

    return merge_sort(leftArr, rightArr)

    return arr
    # if len(arr)<1:return arr
    # mid = len(arr) //2
    # arrA,arrB =  merge_sort(arr[:mid]),merge_sort(arr[mid:])
    # return arr

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

# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    # elements = len(arrA) + len(arrB)
    # merged_arr = [0] * elements
    merged_arr = []

    # Your code here
    x = 0
    y = 0
    while x < len(arrA) and y < len(arrB):
        if arrA[x] < arrB[y]:
            merged_arr.append(arrA[x])
            x+=1
        else:
            merged_arr.append(arrB[y])
            y+=1

    if x == len(arrA):
        merged_arr.extend(arrB[y:])
    else:
        merged_arr.extend(arrA[x:])

    return merged_arr


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort(arr):
    # Your code here
    if len(arr) <= 1:
        return arr

    left, right = merge_sort(arr[:len(arr)//2]), merge_sort(arr[len(arr)//2:])
    arr = merge(left, right)
    return arr




# implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # Your code here


    return arr


def merge_sort_in_place(arr, l, r):
    # Your code here


    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort(arr):
    # Your code here

    return arr

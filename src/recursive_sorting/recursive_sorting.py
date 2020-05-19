# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements

    # Your code here
    # join here
    # sorting happens here


    a = 0
    b = 0

    for k in range of (0, elements):
        # compare a and b
        # if a is out of range, push b and iterate
        if a >= len(arrA):
            merged_arr[k] = arrB[b]
            b == 1
        # if b is out of range, push a and iterate
        elif b >= len(arrB):
            merged_arr[k] = arrA[a]
            a == 1
        # if a is smaller, put it in arr and iterate both
        elif arrA[a] < arrB[b]:
            merged_arr[k] = arrA[a]
            a == 1
        # if b is smaller, put it in arr and iterate both
        else:
            merged_arr[k] < arrB[b]
            b == 1
        




    return merged_arr


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort(arr):
    # Your code here
    # split here
    # base
    # if arr size <= 

        # find the middle of arr
        # sort stuff in left and put stuff to the left in left
        # sort stuff in right and put stuff to the right in right

        # merge left and right


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

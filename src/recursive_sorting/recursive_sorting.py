# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements

    # init the two pointers that start at each list
    a = 0
    b = 0

    while a < len(arrA) and b < len(arrB):
        # compare the elements that a and b point at
        if arrA[a] < arrB[b]:
            combined.append(arrA[a])
            a += 1
        else:
            combined.append(arrB[b])
            b += 1
    # at this point, we've finished traversing one of the lists completely
    # we need to add all of the elements from the other list to the combined list
    while a < len(arrA):
        combined.append(arrA[a])
        a += 1

    while b < len(arrB):
        combined.append(arrB[b])
        b += 1

    return merged_arr


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort(arr):
    # Our base case is when the lists length is 1
    # // is Floor division - division that results into whole number adjusted to the left in the number line
    if len(arr) > 1:
        # Return everything up to the length of the array divided by 2, round down to whole number to the left
        left = merge_sort(arr[:len(arr) // 2])
        # Return everything up to the length of the array divided by 2, round down to whole number to the right
        right = merge_sort(arr[len(arr) // 2:])


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

"""
Recursive sorting assignment file.
"""


def merge(arr_a, arr_b):
    """
    A helper function to merge two arrays.
    """
    elements = len(arr_a) + len(arr_b)
    merged_arr = [0] * elements

    j, k = 0, 0
    for i in range(len(merged_arr)):
        if k > len(arr_b) - 1:
            merged_arr[i] = arr_a[j]
            j += 1
        elif j > len(arr_a) - 1:
            merged_arr[i] = arr_b[k]
            k += 1
        elif arr_a[j] < arr_b[k]:
            merged_arr[i] = arr_a[j]
            j += 1
        elif arr_b[k] < arr_a[j]:
            merged_arr[i] = arr_b[k]
            k += 1

    return merged_arr


def merge_sort(arr):
    """
    Recursive implementation of merge sort.
    """

    if len(arr) <= 1:
        return arr

    arr_a = arr[:len(arr) // 2]
    arr_b = arr[len(arr) // 2:]
    return merge(merge_sort(arr_a), merge_sort(arr_b))


def merge_in_place(arr, start, mid, end):
    """
    An in-place merge helper function.

    The first element of the second sorted section is indicated by 'mid'.
    """

    while start < mid and mid < end + 1:

        if arr[start] < arr[mid]:
            start += 1
        else:
            for i in range(start, mid):
                arr[i], arr[mid] = arr[mid], arr[i]
            start += 1
            mid += 1

    return arr


def merge_sort_in_place(arr, left, right):
    """
    An in-place merge sort implementation.
    """

    if right - left <= 0:
        return arr

    mid = left + ((right - left) // 2)
    merge_sort_in_place(arr, left, mid)
    merge_sort_in_place(arr, mid + 1, right)
    merge_in_place(arr, left, mid + 1, right)

    return arr


def timsort(arr):
    """
    STRETCH: implement the Timsort function below
    hint: check out https://github.com/python/cpython/blob/master/Objects/
    listsort.txt
    """
    # Your code here

    return arr

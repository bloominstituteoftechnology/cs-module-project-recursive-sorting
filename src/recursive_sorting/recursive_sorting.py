# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = []
    # init the two pointers that start at each list
    while len(arrA) > 0 and len(arrB) > 0:
        # compare the elements that a and b point at
        if arrA[0] < arrB[0]:
            merged_arr.append(arrB.pop(0))
        else:
            merged_arr.append(arrA.pop(0))
    # at this point, we've finished traversing one of the lists completely
    # we need to add all of the elements from the other list to the combined list
    while 0 < len(arrA):
        merged_arr.append(arrA.pop(0))
    while 0 < len(arrB):
        merged_arr.append(arrB.pop(0))
    return merged_arr


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    # Our base case is when each lists length is 1
    # // is Floor division - division that results into whole number adjusted to the left in the number line
    mid = len(arr) // 2
    if len(arr) > 1:
        # Return everything up to the length of the array divided by 2, round down to whole number to the left
        left = merge_sort(arr[:mid])
        # Return everything up to the length of the array divided by 2, round down to whole number to the right
        right = merge_sort(arr[mid:])
        # run the left and right through the above "merge" function
        arr = merge(left, right)
    return arr


# implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # begin with the first element in the right
    # half of the list
    half = mid + 1

    # if the two halves we are merging are already sorted
    # we do not have to do anything
    if arr[mid] <= arr[half]:
        return
    # Two pointers to maintain start
    # of both arrays to merge
    while start <= mid and half <= end:
        if arr[start] <= arr[half]:
            start += 1
        else:
            value = arr[half]
            index = half
            # now shift all the element between element 1
            # element 2, right by 1
            while index != start:
                arr[index] = arr[index - 1]
                index -= 1
            arr[start] = value
            # Update all the pointers
            start += 1
            mid += 1
            half += 1
    return arr


# 1 is the for the left index and r is the right index of
# the sub-array of arr to be sorted

def merge_sort_in_place(arr, left, right):
    # Your code here
    if left < right:
        # Split the given array into 2 and create the middle
        middle = left + (right - left) // 2
        # Now sort the left half
        merge_sort_in_place(arr, left, middle)
        # Now sort the right half
        merge_sort_in_place(arr, middle + 1, right)

        merge_in_place(arr, left, middle, right)
    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort(arr):
    # Your code here

    return arr

def merge(arr1, arr2):
    merged_arr = []

    if arr1[-1] > arr2[-1]:
        arr1, arr2 = arr2, arr1

    next_y = iter(arr2)
    y = next(next_y)

    for x in arr1:
        while y < x:
            merged_arr.append(y)
            y = next(next_y)
        merged_arr.append(x)
    merged_arr.append(y)
    merged_arr.extend(next_y)

    return merged_arr


def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2

        left = arr[:mid]
        right = arr[mid:]

        left = merge_sort(left)
        right = merge_sort(right)

        return merge(left, right)

    else:
        return arr


# # STRETCH: implement the recursive logic for merge sort in a way that doesn't
# # utilize any extra memory
# # In other words, your implementation
# should not allocate any additional lists
# # or data structures; it can only re-use the memory it was given as input
#
# def merge_in_place(arr, start, mid, end):
#     # Your code here
#
#
# def merge_sort_in_place(arr, l, r):
#     # Your code here


# TO-DO: Implement a recursive implementation of binary search
def binary_search(arr, target, start, end):

    middle = (start + end) // 2

    if start <= end:

        if len(arr) == 0:
            return -1

        if arr[middle] == target:
            print(arr[middle])
            print(arr.index(arr[middle]))
            return arr.index(arr[middle])

        if arr[middle] > target:
            return binary_search(arr, target, start, (middle - 1))

        if arr[middle] < target:
            return binary_search(arr, target, (middle + 1), end)

    else:
        return -1

        # STRETCH: implement an order-agnostic binary search
        # This version of binary search should correctly find
        # the target regardless of whether the input array is
        # sorted in ascending order or in descending order
        # You can implement this function either recursively
        # or iteratively


def agnostic_binary_search(arr, target):
    pass

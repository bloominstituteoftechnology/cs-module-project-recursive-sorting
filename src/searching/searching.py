# TO-DO: Implement a recursive implementation of binary search
def binary_search(arr, target, start, end):
    if start > end:
        return -1

    else:
        middle = start + end // 2

        guess = arr[middle]

        if guess == target:
            return middle

        elif target > guess:
            return binary_search(arr, target, (middle + 1), end)
        else:
            return binary_search(arr, target, start, (middle - 1))


# STRETCH: implement an order-agnostic binary search
# This version of binary search should correctly find
# the target regardless of whether the input array is
# sorted in ascending order or in descending order
# You can implement this function either recursively
# or iteratively
def agnostic_binary_search(arr, target):
    # Your code here
    pass


arr1 = [-9, -8, -6, -4, -3, -2, 0, 1, 2, 3, 5, 7, 8, 9]
binary_search(arr1, -8, 0, len(arr1)-1)

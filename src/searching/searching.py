# TO-DO: Implement a recursive implementation of binary search
def binary_search(arr, target, start, end):

    if end >= start:
        middle = (start + end) // 2

        if target == arr[middle]:
            return middle

        elif target < arr[middle]:
            end = middle - 1
            return binary_search(arr, target, start, end)

        else:
            start = middle + 1
            return binary_search(arr, target, start, end)

    else:
        return -1


# STRETCH: implement an order-agnostic binary search
# This version of binary search should correctly find 
# the target regardless of whether the input array is
# sorted in ascending order or in descending order
# You can implement this function either recursively 
# or iteratively

def agnostic_binary_search(arr, target):
    start = 0
    end = len(arr) - 1

    order = arr[start] < arr[end]

    while start <= end:
        middle = (start + end) // 2

        if target == arr[middle]:
            return middle

        if order is True:
            if target < arr[middle]:
                end = middle - 1

            else:
                start = middle + 1

        else:
            if target > arr[middle]:
                end = middle - 1

            else:
                start = middle + 1

    return -1


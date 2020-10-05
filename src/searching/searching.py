# TO-DO: Implement a recursive implementation of binary search
def binary_search(arr, target, start, end):
    # cover base cases (no selection, or selection of 1 element)
    if end - start < 0:
        return -1
    elif end - start == 0:
        if arr[start] == target:
            return start
        else:
            return -1

    # check the endpoints
    if arr[start] == target:
        return start
    elif arr[start] > target:
        return -1

    if arr[end] == target:
        return end
    elif arr[end] < target:
        return -1

    # there can't be a middle element to check if the two endpoints are 1 apart
    if end - start == 1:
        return -1

    mid = (start + end) // 2
    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        return binary_search(arr, target, mid + 1, end - 1)
    else:
        return binary_search(arr, target, start + 1, mid - 1)


# STRETCH: implement an order-agnostic binary search
# This version of binary search should correctly find 
# the target regardless of whether the input array is
# sorted in ascending order or in descending order
# You can implement this function either recursively 
# or iteratively
def agnostic_binary_search(arr, target):
    if len(arr) == 0:
        return -1
    
    l = 0
    r = len(arr) - 1

    desc = arr[0] > arr[-1]
    
    if desc:
        if arr[r] > target or arr[l] < target:
            return -1
    else:
        if arr[l] > target or arr[r] < target:
            return -1
    

    if arr[l] == target:
        return l
    elif arr[r] == target:
        return r

    while r - l >= 2:
        mid = (l + r) // 2
        if arr[mid] > target:
            if desc:
                l = mid
            else:
                r = mid
        elif arr[mid] < target:
            if desc:
                r = mid
            else:
                l = mid
        else:
            return mid
    return -1


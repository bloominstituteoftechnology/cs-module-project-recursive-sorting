# TO-DO: Implement a recursive implementation of binary search
def binary_search(arr, target, start, end):
    if start <= end:
        mid = (start + end) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] > target:
            # if element is smaller than mid, then it can be present in left subarray
            return binary_search(arr, target, start, mid-1)
            # else it's in the right side of the array
        else:
            return binary_search(arr, target, mid+1, end)
    else:
        return -1


if __name__ == '__main__':
    arr1 = [-9, -8, -6, -4, -3, -2, 0, 1, 2, 3, 5, 7, 8, 9]
    print(binary_search(arr1, -8, 0, len(arr1)-1))


# STRETCH: implement an order-agnostic binary search
# This version of binary search should correctly find 
# the target regardless of whether the input array is
# sorted in ascending order or in descending order
# You can implement this function either recursively 
# or iteratively
# def agnostic_binary_search(arr, target):

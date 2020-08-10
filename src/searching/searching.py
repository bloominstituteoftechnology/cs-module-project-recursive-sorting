# TO-DO: Implement a recursive implementation of binary search
def binary_search(arr, target, start, end):
    
    if len(arr) == 0:
        return -1

    if start > end:
        return -1

    middle = ((start + end) // 2)

    if arr[middle] == target:
        return middle
    elif arr[middle] < target:
        return binary_search(arr, target, middle+1, end)
    else:
        return binary_search(arr, target, start, middle-1)


# STRETCH: implement an order-agnostic binary search
# This version of binary search should correctly find 
# the target regardless of whether the input array is
# sorted in ascending order or in descending order
# You can implement this function either recursively 
# or iteratively
def agnostic_binary_search(arr, target):
    
    if len(arr) == 0:
        return -1

    is_ascending = (arr[0] < arr[-1])

    if is_ascending == True:
        return binary_search(arr, target, start=0, end=len(arr)-1)
    else:
        output = binary_search(arr[::-1], target, start=0, end=len(arr)-1)
        if output == -1:
            return -1
        else:
            return (len(arr)-1) - binary_search(arr[::-1], target, start=0, end=len(arr)-1)


if __name__ == "__main__":
    descending = [101, 98, 57, 49, 45, 13, -3, -17, -61]
    ascending = [2, 4, 12, 14, 17, 30, 46, 47, 51, 54, 61]
    print(agnostic_binary_search(ascending, 17))
    print(agnostic_binary_search(descending, -1))

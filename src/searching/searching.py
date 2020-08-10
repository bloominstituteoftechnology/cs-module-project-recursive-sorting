# TO-DO: Implement a recursive implementation of binary search
def binary_search(arr, target, left, right):
    # Your code here
    if left > right:
        return -1
    else:
        mid = (left + right) // 2

        if arr[mid] == target:
            return mid

        elif arr[mid] < target:
            return binary_search(arr, target, mid + 1, right)
        else:
            return binary_search(arr, target, left, mid - 1)

arr = [12, 55, 3, 5, 3, 7, 99, 100]
print(binary_search(arr, 99, 0, len(arr)-1))

def decending_binary_search(arr, target, left, right):
    # Your code here
    if left > right:
        return -1
    else:
        mid = (left + right) // 2

        if arr[mid] == target:
            return mid

        elif arr[mid] < target:
            return decending_binary_search(arr, target, left, mid -1)
        else:
            return decending_binary_search(arr, target, mid + 1, right)
# STRETCH: implement an order-agnostic binary search
# This version of binary search should correctly find 
# the target regardless of whether the input array is
# sorted in ascending order or in descending order
# You can implement this function either recursively 
# or iteratively
def agnostic_binary_search(arr, target):
    #Your code here
    if arr[0] > arr[-1]:
        is_ascending = False
    else:
        is_ascending = True
    
    if is_ascending:
        return binary_search(arr, target, 0, len(arr) - 1)
    else: 
        return decending_binary_search(arr, target, 0, len(arr) - 1)


ascending = [2, 4, 12, 14, 17, 30, 46, 47, 51, 54, 61]
descending = [101, 98, 57, 49, 45, 13, -3, -17, -61]

print(agnostic_binary_search(ascending, 12))
print(agnostic_binary_search(ascending, 54))
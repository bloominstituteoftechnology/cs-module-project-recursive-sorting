# TO-DO: Implement a recursive implementation of binary search
def binary_search(arr, target, start, end):
    if start <= end:
        middle_index = int((end + start) / 2)
        guess = arr[middle_index]
        if guess == target:
            return middle_index
        elif guess > target:
            return binary_search(arr, target, start, middle_index - 1)
        else:
            return binary_search(arr, target, middle_index + 1, end)
    return-1

arr = [-9, -8, -6, -4, -3, -2, 0, 1, 2, 3, 5, 7, 8, 9]

print(binary_search(arr, 9, 0, len(arr)-1))


# STRETCH: implement an order-agnostic binary search
# This version of binary search should correctly find 
# the target regardless of whether the input array is
# sorted in ascending order or in descending order
# You can implement this function either recursively 
# or iteratively
# def agnostic_binary_search(arr, target):
#     # Your code here


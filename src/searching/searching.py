# TO-DO: Implement a recursive implementation of binary search
def binary_search(arr, target, start, end):
    # Your code here

    low = start
    high = end

    if len(arr) == 0:
        return -1

    # if low <= high:
    middle = (low + high) // 2
    guess = arr[middle]
        
    if guess == target:
        print(middle)
        return middle

    elif guess > target:
        return binary_search(arr, target, low, high - 1)

    else: 
        return binary_search(arr, target, low + 1, high)

    return -1

# STRETCH: implement an order-agnostic binary search
# This version of binary search should correctly find 
# the target regardless of whether the input array is
# sorted in ascending order or in descending order
# You can implement this function either recursively 
# or iteratively
# def agnostic_binary_search(arr, target):
#     # Your code here


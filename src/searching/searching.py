# TO-DO: Implement a recursive implementation of binary search
def binary_search(arr, target, start, end):

    # Itterative Version

    # low = 0
    # high = len(my_list) - 1

    # while low <= high:
    #     middle = (low + high) // 2
    #             guess = my_list[middle]
    #     if guess == search_item:
    #         return middle
    #     if guess > search_item:
    #         high = middle - 1
    #     else:
    #         low = middle + 1
    # return None

    # Recursive Version

    # Base Case, target = middle
    middle = int(end - start)
    if target == arr[middle]:
        return target

    elif target < arr[middle]:
        binary_search(arr, target, 0, middle)

    elif target > arr[middle]:
        binary_search(arr, target, middle, len(arr) - 1)
        
    return -1 # Target Not Found


# STRETCH: implement an order-agnostic binary search
# This version of binary search should correctly find 
# the target regardless of whether the input array is
# sorted in ascending order or in descending order
# You can implement this function either recursively 
# or iteratively
def agnostic_binary_search(arr, target):
    # Your code here
    pass


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

    # Base Case, target == middle
    if end >= start:
        middle = (end + start) // 2
        if arr[middle] == target:
            return middle
            
        elif arr[middle] > target:
            return binary_search(arr, target, start, middle - 1)
        
        elif arr[middle] < target:
            return binary_search(arr, target, middle + 1, end)

    else:
        return -1 # Target Not Found


# STRETCH: implement an order-agnostic binary search
# This version of binary search should correctly find 
# the target regardless of whether the input array is
# sorted in ascending order or in descending order
# You can implement this function either recursively 
# or iteratively

def descending_binary_search(arr, target, start, end):
    # Base Case, target == middle
    if end >= start:
        middle = (end + start) // 2
        if arr[middle] == target:
            return middle
            
        elif arr[middle] < target:
            return descending_binary_search(arr, target, start, middle - 1)
        
        elif arr[middle] > target:
            return descending_binary_search(arr, target, middle + 1, end)

    else:
        return -1 # Target Not Found

def agnostic_binary_search(arr, target):
    if arr[0] < arr[-1]:
        return binary_search(arr, target, 0, len(arr) - 1)
    else:
        return descending_binary_search(arr, target, 0, len(arr) - 1)

if __name__ == "__main__":
    ascending = [2, 4, 12, 14, 17, 30, 46, 47, 51, 54, 61]
    descending = [101, 98, 57, 49, 45, 13, -3, -17, -61]

    print(agnostic_binary_search(ascending, 12))
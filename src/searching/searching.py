# TO-DO: Implement a recursive implementation of binary search
def binary_search(arr, target, start, end):
    # start = len(arr) - 1
    # end = 0
    # while end <= start:
    #     middle = (end + start) // 2
    #     temp = arr[middle]
    #     if temp == target:
    #         return middle
    #     if temp > target:
    #         start = middle - 1
    #     else:
    #         end = middle + 1
    # return -1
    
        # base case 
        if len(arr) == 0:
            return -1
        
        elif len(arr) == 1:
            if arr[0] == target:
                return 0
            else:
                return -1
        else:
            mid = (start + end) // 2
            if arr[mid] == target:
                return mid
            elif arr[mid] < target:
                return binary_search(arr, target, mid+1, end)
            else:
                return binary_search(arr, target, start, mid-1)
     
          
                


# Your code here
# pass


# STRETCH: implement an order-agnostic binary search
# This version of binary search should correctly find
# the target regardless of whether the input array is
# sorted in ascending order or in descending order
# You can implement this function either recursively
# or iteratively
def agnostic_binary_search(arr, target):
    # Your code here
    pass

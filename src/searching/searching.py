# TO-DO: Implement a recursive implementation of binary search
def binary_search(arr, target, start, end):
    #base case if the first the same as the last
    if start > end:
        return -1

    # get the middle
    middle = (start + end) // 2

    # base case (item found in middle spot)
    if target == arr[middle]:
        return middle

    else:
        #  if not found, split in half depending on which side it is
        if target < arr[middle]:
            #arr = arr[:middle]
            # change the last if on the left
            end = middle - 1
        else:
            # change the first if on the right
            #arr = arr[]
            start = middle + 1
        # call itself
        return binary_search(arr, target, start, end)


# STRETCH: implement an order-agnostic binary search
# This version of binary search should correctly find 
# the target regardless of whether the input array is
# sorted in ascending order or in descending order
# You can implement this function either recursively 
# or iteratively
def agnostic_binary_search(arr, target):
    # Your code here
    pass

arr1 = [-9, -8, -6, -4, -3, -2, 0, 1, 2, 3, 5, 7, 8, 9]

print(binary_search(arr1, -8, 0, len(arr1)-1))
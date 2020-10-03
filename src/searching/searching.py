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
    #check to see what order it's in 
    first = arr[0]
    last = arr[len(arr) - 1]
    
    #if in ascending order do a regular binary search
    if first < last:
        return binary_search(arr, target, 0, len(arr)-1)
    # otherwise send in the number backwards
    else:
        first = 0
        last = (len(arr) - 1)
        found = False

        while first <= last and not found:
            middle = (first + last) // 2
            
            if target == arr[middle]:
                found = True
                return middle
            else:
                if target > arr[middle]:
                    last = middle - 1
                else:
                    first = middle + 1
        return -1 

ascending = [2, 4, 12, 14, 17, 30, 46, 47, 51, 54, 61]
descending = [101, 98, 57, 49, 45, 13, -3, -17, -61]

print(agnostic_binary_search(descending, 49))
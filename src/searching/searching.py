# TO-DO: Implement a recursive implementation of binary search
def binary_search(arr, target, start, end):
    
    # Check if the target is less than or equal to the end (so we know if it exists in the array)
    if target <= end:
        # Get the mid point
        mid_point = (start + end) // 2 # the '//' give a rounded answer if there is a remainder

        # Check if the mid_point is the target  --- Base case.
        if arr[mid_point] == target :
            return mid_point
        
        # If the target is smaller than the mid_point, then recurse on the left side (the smaller side)
        elif target < arr[mid_point]:
            # Set a new end to pass to the recuresive call which is one less than the current mid point
            small_end = mid_point - 1
            return binary_search(arr, target, start, small_end)  # -- move to base case

        # Otherwise the target must be on the right side (the larger side)
        else:
            # Set a new start to pass to the recuresive call which is one more than the current mid point
            large_start = mid_point + 1
            return binary_search(arr, target, large_start, end) # -- move to base case

    else:
        return -1


# STRETCH: implement an order-agnostic binary search
# This version of binary search should correctly find 
# the target regardless of whether the input array is
# sorted in ascending order or in descending order
# You can implement this function either recursively 
# or iteratively
# def agnostic_binary_search(arr, target):
    # Your code here


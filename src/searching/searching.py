# TO-DO: Implement a recursive implementation of binary search
def binary_search(arr, target, start, end):
    # the base case
    if start > end:
        return -1
    # pick the middle
    point = start + ((end - start)//2)

    if arr[point] == target:
        return point
    if arr[point] > target:
        # need to go left here
        end = point -1
    else:
        start = point + 1
    return binary_search(arr, target, start, end)
    


# STRETCH: implement an order-agnostic binary search
# This version of binary search should correctly find 
# the target regardless of whether the input array is
# sorted in ascending order or in descending order
# You can implement this function either recursively 
# or iteratively

# This is the comparator that I made that will
# return 0 to mean go left and 1 to mean go right
def comparator(target_val, point_chosen_val, ascending=True):
    if ascending: # this is ascending order
        if target_val < point_chosen_val:
            return 0 # this means to to left
        else:
            return 1 # go right
    else: # descending
        if target_val > point_chosen_val:
            return 0 # Go left
        else:
            return 1 # go right



def binary_search_inner(arr, target, start, end, ascending=True):
    # base case
    if start > end:
        return -1
    # moving to the middle of the start and the end
    pt_chosen = start + ((end - start)//2)
    if arr[pt_chosen] == target:
        return pt_chosen
    else:
        # figuring which way to travel
        if comparator(target_val=target, ascending=ascending, point_chosen_val=arr[pt_chosen]) == 0:
            # means to go left
            end = pt_chosen -1
        else:
            # in here means to go right
            start = pt_chosen + 1
    return binary_search_inner(arr, target, start, end, ascending)



def agnostic_binary_search(arr, target):
    # creating the binary search that is order agnostic
    # I am making this method to call the one above and 
    # be a wrapper of the method above
    
    # first will be checking to see if the arr is empty
    if len(arr) == 0:
        return False
    
    # will check to see if the who is the larger value
    # the first or the last
    if arr[0] <= arr[len(arr)-1]:
        # This means that we have ascending order
        return binary_search_inner(arr, target, start=0, end=len(arr)-1, ascending=True)
    else:
        return binary_search_inner(arr, target, start=0, end=len(arr)-1, ascending=False)


# TO-DO: Implement a recursive implementation of binary search
def binary_search(arr, target, start, end):
    # Your code here
    middle = (start+end)//2
    if arr[middle] == target:
        return middle
    elif  target < arr[middle]:
        middle = binary_search(arr,target,start,middle-1)
    elif target > arr[middle]:
        middle = binary_search(arr,target,middle+1,end)
    return middle

listy = [1,2,3,4,5,6,7,8,9]

print(binary_search(listy, 8, 0, 8))
    



# STRETCH: implement an order-agnostic binary search
# This version of binary search should correctly find 
# the target regardless of whether the input array is
# sorted in ascending order or in descending order
# You can implement this function either recursively 
# or iteratively
# def agnostic_binary_search(arr, target):
    # Your code here


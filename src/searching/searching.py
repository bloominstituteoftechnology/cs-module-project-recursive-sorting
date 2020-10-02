# TO-DO: Implement a recursive implementation of binary search
# TO-DO: Implement a recursive implementation of binary search
def binary_search(arr, target, start, end):

  if arr == []:
    return []

  middle = int((start + end) / 2)

  if target < arr[start] or target > arr[end]:
    return "Not found"

  if target == arr[middle]:
    return middle
  elif target < arr[middle]:
    return binary_search(arr, target, start, middle-1)
  elif target > arr[middle]:
    return binary_search(arr, target, middle+1, end)
  else:
    return "Not found"

# arr = [-9, -8, -6, -4, -3, -2, 0, 1, 2, 3, 5, 7, 8, 9]
# arr2 = []
# print(binary_search(arr, 4, 0, len(arr)-1))


# STRETCH: implement an order-agnostic binary search
# This version of binary search should correctly find 
# the target regardless of whether the input array is
# sorted in ascending order or in descending order
# You can implement this function either recursively 
# or iteratively
def agnostic_binary_search(arr, target):
    # Your code here


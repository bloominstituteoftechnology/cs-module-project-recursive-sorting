# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements

    # Your code here


    return merged_arr



# TO-DO: implement the Merge Sort function below recursively
def merge_sort(arr):
  if len(arr)>1:
    mid = len(arr)//2
    left = arr[:mid]
    right = arr[mid:]

    left = merge_sort(left)
    right = merge_sort(right)

    arr = []

    while len(left) > 0 and len(right) > 0:
      if left[0] < right[0]:
        arr.append(left[0])
        left.pop(0)
      else:
        arr.append(right[0])
        right.pop(0)

    for i in left:
      arr.append(i)
    for i in right:
      arr.append(i)

  return arr

arr = [5, 3, 7, 3, 6, 12, 15, 53]
print(arr)
arr1 = merge_sort(arr)
print(arr1)

# STRETCH: implement the recursive logic for merge sort in a way that doesn't 
# utilize any extra memory
# In other words, your implementation should not allocate any additional lists 
# or data structures; it can only re-use the memory it was given as input
def merge_in_place(arr, start, mid, end):
    # Your code here
    pass


def merge_sort_in_place(arr, l, r):
    # Your code here
    pass


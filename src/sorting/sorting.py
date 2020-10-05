# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements

    left_array = 0
    right_array = 0
    index = 0

    while left_array < len(arrA) and right_array < len(arrB):
        if arrA[left_array] < arrB[right_array]:
            merged_arr[index] = arrA[left_array]
            left_array += 1
        else:
            merged_arr[index] = arrB[right_array]
            right_array += 1
        
        index += 1

    while left_array < len(arrA):
        merged_arr[index] = arrA[left_array]
        left_array += 1
        index += 1

    while right_array < len(arrB):
        merged_arr[index] = arrB[right_array]
        right_array += 1
        index += 1

    return merged_arr



# TO-DO: implement the Merge Sort function below recursively
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]

        left = merge_sort(left)
        right = merge_sort(right)

        return merge(left, right)

    return arr

arr = [5, 3, 7, 3, 6, 12, 15, 53]
print(arr)
print(merge_sort(arr))

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

# arr = []

    # while len(left) > 0 and len(right) > 0:
    #   if left[0] < right[0]:
    #     arr.append(left[0])
    #     left.pop(0)
    #   else:
    #     arr.append(right[0])
    #     right.pop(0)

    # for i in left:
    #   arr.append(i)
    # for i in right:
    #   arr.append(i)


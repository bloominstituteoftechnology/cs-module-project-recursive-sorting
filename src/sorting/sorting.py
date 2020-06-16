# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements

    # Your code here
    # index for arrA
    arrA_index = 0
    # index for arrB
    arrB_index = 0
    # loop through merged_arr
    for i in range(elements):
        print(merged_arr)
        # check if
        if arrA_index < len(arrA) and arrB_index < len(arrB):
            # check which value is less than
            if arrA[arrA_index] <= arrB[arrB_index]:
                # set smaller value in sorted list and increment count for appropriate list
                merged_arr[i] = arrA[arrA_index]
                arrA_index += 1
            else:
                merged_arr[i] = arrB[arrB_index]
                arrB_index += 1
        # check for potentially one array to have all elements added already
        elif arrA_index < len(arrA) and arrB_index is len(arrB):
            merged_arr[i] = arrA[arrA_index]
            arrA_index += 1
        else:
            merged_arr[i] = arrB[arrB_index]
            arrB_index += 1
    # return sorted list
    return merged_arr

foo = [2, 5, 8, 9, 10]
foobar = [1, 3, 4, 6, 7]
x = merge(foo, foobar)
print(x)
foo = [7, 87]
foobar = [12, 90]
x = merge(foo, foobar)
print(x)
# TO-DO: implement the Merge Sort function below recursively
def merge_sort(arr):
    # Your code here
    # if input list is greater than 1 then take length devided by 2 rounded
    if len(arr) > 1:
        # half index for the array
        half = len(arr) // 2
        # split list into left half (start to half)
        left = arr[: half]
        # split list into right half (half to end)
        right = arr[half:]
        # half until left is down to 1 item in left list
        left = merge_sort(left)
        # half until left is down to 1 item in right list
        right = merge_sort(right)
        # return sorted list 
        return merge(left, right)
    
    # if input list has 1 element then its already sorted, YEET!
    return arr


foo = [9, 5, 8, 2, 10, 3, 7, 1, 4, 6]
sorted_list = merge_sort(foo)
print(sorted_list)
# STRETCH: implement the recursive logic for merge sort in a way that doesn't 
# utilize any extra memory
# In other words, your implementation should not allocate any additional lists 
# or data structures; it can only re-use the memory it was given as input
# def merge_in_place(arr, start, mid, end):
#     # Your code here


# def merge_sort_in_place(arr, l, r):
#     # Your code here


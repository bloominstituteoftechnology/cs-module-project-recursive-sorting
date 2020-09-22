# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements

    # Your code here
    cur_index = 0
    arrA_index = 0
    arrB_index = 0
    while cur_index < elements:

        if arrA_index < len(arrA) and arrB_index < len(arrB):
            if arrA[arrA_index] < arrB[arrB_index]:
                merged_arr[cur_index] = arrA[arrA_index]
                arrA_index += 1
                cur_index += 1

            else: 
                merged_arr[cur_index] = arrB[arrB_index]
                arrB_index += 1 
                cur_index += 1

        elif arrA_index == len(arrA):
            merged_arr[cur_index] = arrB[arrB_index]
            arrB_index += 1
            cur_index += 1


        elif arrB_index == len(arrB):
            merged_arr[cur_index] = arrA[arrA_index]
            arrA_index += 1
            cur_index += 1
        else:
            print("Biatch")
            
            
            
    return merged_arr
# wapOne = [2,5,6,7,13,22]
# wapTwo = [6,9,17,25,30,60]
# newARRAY = merge(wapOne, wapTwo)

# TO-DO: implement the Merge Sort function below recursively
def merge_sort(arr):
    # Your code here

    if len(arr) > 1:
        m = len(arr) // 2
        left = merge_sort(arr[:m])
        right = merge_sort(arr[m:])
        print(f"{left} {right}")

    else:
        return arr 

    return merge(left, right)

#     return arr

# # STRETCH: implement the recursive logic for merge sort in a way that doesn't 
# # utilize any extra memory
# # In other words, your implementation should not allocate any additional lists 
# # or data structures; it can only re-use the memory it was given as input
# def merge_in_place(arr, start, mid, end):
#     # Your code here


# def merge_sort_in_place(arr, l, r):
#     # Your code here


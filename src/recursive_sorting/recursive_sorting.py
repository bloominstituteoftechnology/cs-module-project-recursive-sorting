# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements
   
    a_marker = 0
    b_marker = 0
    i = 0;

    while a_marker < len(arrA) and b_marker < len(arrB):
        # compare the elements that a and b point at
        if arrA[a_marker] < arrB[b_marker]:
            merged_arr[i] = arrA[a_marker]
            a_marker += 1
            i +=1
        else:
            merged_arr[i] = arrB[b_marker]
            b_marker += 1
            i +=1
            
    # # check left side
    # while a_marker < len(arrA):
    #     if arrA[a_marker] < arrB[b_marker]:
    #         merged_arr[i] = arrA[a_marker]
    #         a_marker += 1
    #         i +=1
    #     else:
    #         merged_arr[i] = arrB[b_marker]
    #         b_marker += 1
    #         i +=1
    
    # # check right side
    # while b_marker < len(arrB):
    #     if arrB[b_marker] < arrA[a_marker]:
    #         merged_arr[i] = arrA[b_marker]
    #         b_marker += 1
    #         i +=1
    #     else:
    #         merged_arr[i] = arrB[b_marker]
    #         b_marker += 1
    #         i +=1

    

    # at this point at least 1 of the lists have been traversed completely
    # we need to ensure that the other list is also added to the merged arr
    if a_marker < len(arrA):
        while a_marker < len(arrA):
            merged_arr[i] = arrA[a_marker]
            a_marker += 1
            i +=1
    else:
        while b_marker < len(arrB):
            merged_arr[i] = arrB[b_marker]
            b_marker += 1
            i +=1
        
    print(f'merged array: {merged_arr}')
    return merged_arr


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort(arr):
    # break the array down recursively
    # base case: when the lists get down to lengths of 1
 
    if len(arr) > 1:
        left = merge_sort(arr[:len(arr)//2])
        right = merge_sort(arr[len(arr)//2:])
        arr = merge(left,right)

    # merge them back up
    return arr

my_list = [1,4,3,5,9,7,8,2,6]
print(merge_sort(my_list))



# implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # Your code here


    return arr


def merge_sort_in_place(arr, l, r):
    # Your code here


    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort(arr):
    # Your code here

    return arr

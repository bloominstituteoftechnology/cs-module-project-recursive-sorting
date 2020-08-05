# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements

    # assigning the pointer for both of the arrays
    a_ptr = 0
    b_ptr = 0
    m_ptr = 0
    # doing a while loop
    while a_ptr < len(arrA) and b_ptr < len(arrB):
        if arrA[a_ptr] <= arrB[b_ptr]:
            # putting in the point in the left array
            # and then incrementing the pointer
            merged_arr[m_ptr] = arrA[a_ptr]
            a_ptr +=1
        else: # putting the element that is in the rArr
            merged_arr[m_ptr] = arrB[b_ptr]
            b_ptr +=1
        # incrementing the merged_arr pointer
        m_ptr +=1
    # once we are out of the loop we will then add one or the other array to the 
    # merged array
    while a_ptr < len(arrA):
        merged_arr[m_ptr] = arrA[a_ptr]
        a_ptr += 1
        m_ptr += 1
    while b_ptr < len(arrB):
        merged_arr[m_ptr] = arrB[b_ptr]
        b_ptr += 1
        m_ptr += 1
    return merged_arr



    

# TO-DO: implement the Merge Sort function below recursively
def merge_sort(arr):
    # put the base case
    # doing the lenght just once
    n = len(arr)
    if n < 2:
        return arr
    # will  divide the arr into 2 and then call
    # the merge sort on both of them
    mid = n//2
   
    lArr = arr[:mid]
    rArr = arr[mid:]
    # now calling merge_sort on both
    lArr  = merge_sort(lArr)
    rArr  = merge_sort(rArr)
    # now calling the merge this will work on the two arrays that 
    # come back from the merg_sort algorithm
    arr = merge(lArr, rArr)
    return arr

# STRETCH: implement the recursive logic for merge sort in a way that doesn't 
# utilize any extra memory
# In other words, your implementation should not allocate any additional lists 
# or data structures; it can only re-use the memory it was given as input
def merge_in_place(arr, start, mid, end):
    # doing the merge_in_place
    rStart = mid
    l = start

    while l < mid and rStart < end +1:
        # doing the swaping if it is needed
        if arr[rStart] < arr[l]:
            #  put the r into the left side
            temp = arr[l]
            arr[l] = arr[rStart]
            arr[rStart] = temp
            # will then need to increment the l
            
        
        l +=1
            

def merge_sort_in_place(arr, l, r):
    # the base case is when the left and the right are equal to 
    # each other
    if l == r:
        return l,r
    
    # we will find the middle point where we want to split the arr
    length = 1 + (r - l)
    mid =  l + (length//2)
    # will then be calling the merge_sort_in_place on each of the halves
    leftStart ,lend = merge_sort_in_place(arr, l, r=mid-1)
    rstart, rightend = merge_sort_in_place(arr, l=mid, r=r)
    # Will now call the merge_in_place function
    # start is the left start, mid will be the rightStart, end will be right end
    
    mid = (1 + (rightend - leftStart)) //2

    merge_in_place(arr, start=leftStart, mid=rstart, end=rightend)

    return leftStart, rightend

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
    # creating a base case
    if start == end:
        return
    breakpoint()
    lpt = mid -1
    rpt = mid
    need_rotate = False
    # It will go in here if we need to do iterative swapping
    if lpt == start or rpt == end:
        lpt = start +1
        while lpt <= end:
        if arr[lpt] < arr[start]:
            temp = arr[lpt]
            arr[lpt] = arr[start]
            arr[start] = temp
        return
    # tyring to do the merge in place
    # pick the middle and move outward till we 
    # find one on the l side that is less
    # this here is for when there are more than 2 in length
    while lpt >=start and rpt <= end:
        if lpt < rpt:
            need_rotate = True
            break
        # move them closer to the middle
        lpt -=1
        rpt +=1
    # Will rotate those indices that are between the lpt and the rpt
    if need_rotate == False:
        return 

    # Will do the swapping of the elements
    if lpt == mid-1:
        swapto = lpt
        swapfrom =rpt
    else:
        swapto = lpt +1
        swapfrom = mid
    while need_rotate:
        temp = arr[swapto]
        arr[swapto] = arr[swapfrom]
        arr[swapfrom] = temp
        swapfrom +=1
        swapto += 1
        if swapto >= mid:
            need_rotate = False
    # calling this same call again recursively for the left and the right side
    # left side
    #lend =mid -1
    #l_mid = start + (1+(lend - start ))//2
    #r_mid = mid + (1 + (end - mid))//2
    #merge_in_place(arr, start=start,  mid=l_mid, end=lend)
    #merge_in_place(arr, start=mid, mid=r_mid, end=end)
    #breakpoint()
    #while l < mid or end >= mid:
    #    # doing the swaping if it is needed
    #    if arr[mid] < arr[l] and l < mid:
    #        #  put the r into the left side
    #        temp = arr[l]# 
    #        arr[l] = arr[mid]
    #        arr[mid] = temp
    #        # will then need to increment the l
    #        
    #    if arr[end] < arr[leftBig] and end >= mid:
    #        # will be doing the swapping of the
    #        # to put the largest number/item in 
    #        # the end. and then will decrement the 
    #        # end.
    #        temp = arr[end]
    #        arr[end] = arr[leftBig]
    #        arr[leftBig] = temp
    #    end -=1
    #    l +=1
        
        
        
            

def merge_sort_in_place(arr, l, r):
    # the base case is when the left and the right are equal to 
    # each other
    if l == r:
        return  l,r
    # we will find the middle point where we want to split the arr
    length = 1 + (r - l)
    mid =  l + (length//2)
   # will then be calling the merge_sort_in_place on each of the halves
    leftStart ,lend = merge_sort_in_place(arr, l, r=mid-1)
    rstart, rightend = merge_sort_in_place(arr, l=mid, r=r)
   # Will now call the merge_in_place function
   # start is the left start, mid will be the rightStart, end will be right end
   
    mid = leftStart + ((1 + (rightend - leftStart)) //2)
    merge_in_place(arr, start=leftStart, mid=rstart, end=rightend)
    return leftStart, rightend

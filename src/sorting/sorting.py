# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements
    i=j = k = 0
    while i < len(arrA) and j < len(arrB):
    #compare two array
        if arrA[i] > arrB[j]:
            #store smaller element
            merged_arr[k] = arrB[j]
            j +=1
        else:
            merged_arr[k] = arrA[i]
            i +=1
        k +=1
    #store remaining element of first array
    while i < len(arrA):
        merged_arr[k] = arrA[i]
        i +=1
        k +=1 

    #store remaining element of second array
    while j < len(arrB):
        merged_arr[k] = arrB[j]
        k += 1
        j +=1
    
    return merged_arr

# TO-DO: implement the Merge Sort function below recursively
def merge_sort(arr):
    
    #if length of array is grater than 1
     #sliced  the array in to halves
    if len(arr)<=1:
        return arr
        #Find the the middle part of the arr
    mid = len(arr)//2
    left_array = arr[:mid]
    right_array = arr[mid:]
    # resursive call the function on left and right array 
    x= merge_sort(left_array)
    y = merge_sort(right_array)
    #merge sorted piece
    arr =  merge(x, y)
    print(f'FIRST Merge: {arr}')
        
            
    return arr

myList = [83, 20, 9, 50, 115, 61, 17]
merge_sort(myList)
#print(myList)
#print(merge_sort(arr1))

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

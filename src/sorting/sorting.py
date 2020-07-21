# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    #merged_arr = [0] * elements
    merged_arr = []

    #Your code here
    # for element in arrA:
    #     merged_arr.append(element)
    # for element in arrB:
    #     merged_arr.append(element)
    """
    [1 4 7]
    [2 8 9]

    arrA[0] arrB[0]
    [4 7]
    [2 8 9]
    out [1]

    min arrA[0] arrB[0]
    [4 7]
    [8 9]
    out [1 2]

    min arrA[0] arrB[0]
    [7]
    [8 9]
    out [1 2 4]

    min arrA[0] arrB[0]
    []
    [8 9]
    out [1 2 4 7]

    len(arrA)== 0 
    []
    [9]
    out [1 2 4 7 8]
    """
    while len(arrA) > 0 or len(arrB) > 0:
        if len(arrA) == 0:
            merged_arr.append(arrB[0])
            arrB.pop(0)
            
        elif len(arrB) == 0:
            merged_arr.append(arrA[0])
            arrA.pop(0)

        elif arrA[0] < arrB[0]:
            merged_arr.append(arrA[0])
            arrA.pop(0)
            print(arrA)
        else:
            merged_arr.append(arrB[0])
            arrB.pop(0)
            print(arrB)
        print(f'mergedarray {merged_arr}')

    return merged_arr

# TO-DO: implement the Merge Sort function below recursively
def merge_sort(arr):
    # Your code here
    #print(f'The Array: {arr}')

    if len(arr) <= 1: ## base case
        return arr
    # divide in half until I have sub arrays of length 1

    #print(int(len(arr)/2))
    
        ## recursively splitting the array
    left_arr = arr[0:int(len(arr)//2)]
    right_arr = arr [int(len(arr))//2:int((len(arr)))]

    left_arr = merge_sort(left_arr)
    
    right_arr = merge_sort(right_arr)
    print(f'left arr {left_arr}')
    print(f'right arr {right_arr}')

    sorted_array = merge(left_arr, right_arr)

        #if len(left_arr) == 0 and len(right_arr) == 0:

        # if left_arr[0] < right_arr[0]:
        #     sorted_arr = [left_arr[0], right_arr[0]]
        # else: # if right array < left array
        #     sorted_arr = [right_arr[0], left_arr[0]]

        # print(f'sorted array {sorted_arr}')



    
    # merge them back in, switching orders to sort


    return sorted_array





## divide into two (recursion)
## until they're lists by themselves (base case)



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


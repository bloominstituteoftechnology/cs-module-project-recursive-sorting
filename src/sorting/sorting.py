# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements
    print(merged_arr)
    # Your code here


    return merged_arr

# TO-DO: implement the Merge Sort function below recursively
def merge_sort(arr):
    # Your code here
    # base case: list has one or fewer elements
    #recursive case: list has two or more elements
    if len(arr) > 1:
        middle = len(arr) // 2
        low = arr[:middle]
        high = arr[middle:]
        k = []

        merge_sort(low)
        merge_sort(high)
        print(low)
        print(high)

        i = j = 0

        while i < len(high) and j < len(low):
            if low[i] < high[j]:
                k.append(low[i])
                i += 1
            else:
                k.append(high[j])
                j += 1

        while i < len(low):
            k.append(low[i])
            i += 1

        while j < len(high):
            k.append(high[j])
            j += 1



    return arr

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

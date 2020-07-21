# TO-DO: Implement a recursive implementation of binary search
def binary_search(arr, target, start, end):
    '''
    This will return the INDEX of a target if it's found in the array,
    otherwise it will return -1
    '''
    # Your code here
    first_index = start
    last_index = end
    middle_index = (first_index + last_index) // 2

    print(f'first index {first_index}')
    print(f'last index {last_index}')
    print(f' middle index {middle_index}')
    print(f'target {target}')
    print(f'OG arr {arr}')

    if end >= start:
        print("-----------")

        #update middle_index
        middle_index = (start + end) // 2
        #print(f'array at middle index {arr[middle_index]}')

        ## if target IS the middle index, return middle index
        if target == arr[middle_index]:
            print(f'!!!!!!!!!middle index {middle_index}')
            return middle_index

        elif target < arr[middle_index]:   
            #arr = arr[start:end]
            return binary_search(arr=arr, target=target, start=start, end=middle_index)
        else:
            return binary_search(arr=arr, target=target, start=middle_index, end=end)
        
    return -1


    # lookup_arr = arr

    # ## if target IS the middle index, return middle index
    # while len(arr) >= 1:
    #     print("-----------")
    #     print(f'array at middle index {arr[middle_index]}')
    #     if target == arr[middle_index]:
    #         print(f'!!!!!!!!!middle index {middle_index}')
    #         return middle_index

    #     elif target < arr[middle_index]:
    #         end = middle_index
    #         middle_index = (first_index + end) // 2
    #         arr = arr[start:end]
    #         return binary_search(arr, target, start, end)
        
    # return -1







# STRETCH: implement an order-agnostic binary search
# This version of binary search should correctly find 
# the target regardless of whether the input array is
# sorted in ascending order or in descending order
# You can implement this function either recursively 
# or iteratively
def agnostic_binary_search(arr, target):
    # Your code here
    pass


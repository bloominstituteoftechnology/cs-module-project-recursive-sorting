# TO-DO: complete the helper function below to merge 2 sorted arrays

def create_array(size=8, max=50):
    from random import randint
    return [randint(0, max) for _ in range(size)]

# TO-DO: implement the Merge Sort function below recursively


def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements

    arrA_pointer = arrB_pointer = 0

    arrA_length, arrB_length = len(arrA), len(arrB)

    for _ in range(elements):  # 8 elements of at value of 0 array
        if arrA_pointer < arrA_length and arrB_pointer < arrB_length:  # base case
            if arrA[arrA_pointer] <= arrB[arrB_pointer]:
                merged_arr[arrA_pointer + arrB_pointer] = arrA[arrA_pointer]
                arrA_pointer += 1

            else:
                merged_arr[arrA_pointer + arrB_pointer] = arrB[arrB_pointer]

                arrB_pointer += 1

        elif arrA_pointer == arrA_length:
            # right array
            merged_arr[arrA_pointer + arrB_pointer] = arrB[arrB_pointer]
            arrB_pointer += 1

        elif arrB_pointer == arrB_length:
            merged_arr[arrA_pointer +
                arrB_pointer] = arrA[arrA_pointer]  # left array
            arrA_pointer += 1

    return merged_arr


# test case
a = [1, 3, 5]
b = [2, 4, 6]


def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    midpoint = int(len(arr) // 2)

    arrA = merge_sort(arr[:midpoint])
    arrB = merge_sort(arr[midpoint:])

    return merge(arrA, arrB)


# verify it works
a = create_array()
b = create_array()
print(a)
print(b)

s = merge_sort(a + b)
print(s)


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

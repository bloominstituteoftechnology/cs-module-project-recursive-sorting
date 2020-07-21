# Debt to: https://www.youtube.com/watch?v=3aTfQvs-_hA
def merge(arrA, arrB):
    output = []
    # i <- index of arrA
    # j <- index of arrB
    i, j = 0, 0
    # Appends whichever of the leftmost elements of the arrays
    # is smallest into the output arry.
    while i < len(arrA) and j < len(arrB):
        if arrA[i] < arrB[j]:
            output.append(arrA[i])
            i += 1

        else:
            output.append(arrB[j])
            j += 1

    if i == len(arrA):
        output.extend(arrB[j:])
    else:
        output.extend(arrA[i:])

    return output

def merge_sort(arr):
    # Base Case
    if len(arr) <= 1:
        return arr

    # Recursively spits the arrays into halves,
    # creating single-element arrays.
    left, right = merge_sort(arr[:len(arr) // 2]), merge_sort(arr[len(arr) // 2:])
    # Merges the split arrays itteratively, taking the smallest
    # elements first.
    return merge(left, right)

# STRETCH: implement the recursive logic for merge sort in a way that doesn't 
# utilize any extra memory
# In other words, your implementation should not allocate any additional lists 
# or data structures; it can only re-use the memory it was given as input
def merge_in_place(arr, start, mid, end):
    pass



def merge_sort_in_place(arr, l, r):
    pass


if __name__ == "__main__":
    array1 = [1, 5, 8, 4]
    array2 = [2, 9, 6, 0, 3, 7]

    print(merge(array1, array2))
    print(merge_sort(array1 + array2))
    
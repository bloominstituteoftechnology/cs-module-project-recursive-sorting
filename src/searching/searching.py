# TO-DO: Implement a recursive implementation of binary search
def binary_search(arr, target, l, h, r=False):
    # Your code here
    m = (l + h) // 2
    print('l', l, 'h', h, 'm', m)
    if arr[m] == target:
        return m
    elif arr[m] < target:
        if r: l = m + 1
        else: l = m
    else:
        if r: h = m
        else: h = m + 1
    if r is True and l < h:
        return binary_search(arr, target, l, h, r)
    elif r is False and h <= l:
        return binary_search(arr, target, l, h, r)
    else:
        return -1

arr = [3, 7, 10, 12, 22, 99]
arr.reverse()
print(arr)
# print(binary_search(arr, 2, 0, len(arr) - 1))

# STRETCH: implement an order-agnostic binary search
# This version of binary search should correctly find 
# the target regardless of whether the input array is
# sorted in ascending order or in descending order
# You can implement this function either recursively 
# or iteratively
def agnostic_binary_search(arr, target):
    l, h, r = 0, len(arr) - 1, True
    if arr[l] > arr[h]:
        l, h = h, l
        r = False
    return binary_search(arr, target, l, h, r)

print(agnostic_binary_search(arr, 3))

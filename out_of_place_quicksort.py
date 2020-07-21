'''
Out-of-place Quicksort
'''


def partition(data):
    # Partition the data
    # Start by choosing a pivot (choose the first item in the list)
    pivot = data[0]
    # We need to create storage for the LHS and the RHS
    left = []
    right = []


​
  # We need to loop through each item
  for current in data[1:]:
       # if it's smaller or equal, append to left
       if current <= pivot:
            left.append(current)
        # if it's bigger, add to RHS storage
        else:
            right.append(current)
​
  return left, right, pivot
​
​
# What kind of input will we get?
# We expect a list


def quicksort(data):
    # check if data has 1 or 0 elements
    # (base case) a side only contains a single element
    if len(data) <= 1:
        return data


​
  left, right, pivot = partition(data)
​
  # (recursive case) Recursively Quick Sort LHS and RHS until
  return quicksort(left) + [pivot] + quicksort(right)
​
​
quicksort([2, 5, 7,1,3,4,6,9,8])


# helper function conceptual partitioning
def partition(data):
  # takes in a single list and partitions it into a tuple: (left, pivot, right)
  # create 2 empty lists (left and right)
  left = []
  right = []
  # create a pivot containing the selected pivot point
  pivot = data[0]
  
  # for each value in our data starting at index[1]
  for value in data[1:]:
    # check if value is <= our pivot
    if value <= pivot:
      # append to left hand list
      left.append(value)
    # else value is > our pivot
    else:
      # append to right hand list
      right.append(value)
  
  # return the tuple of (left, pivot, right)
  return left, pivot, right

def quick_sort(data):
  #  base case if the data is an empty list return an empty list
  if data == []:
    return data

  # partition the data into 3 variables: (left, pivot, right)
  left, pivot, right = partition(data)
  
  # recursive call to quick_sort() using the left
  # recursive call to quick_sort() using the right
  # return the concatentation quick_sort of lhs + pivot + quick_sort of rhs
  return quick_sort(left) + [pivot] + quick_sort(right)

list = [4, 5, 2, 4, 54, 3, 12, 5, 7, 3]

print(list)
sorted_list = quick_sort(list)
print(sorted_list)

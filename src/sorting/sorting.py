# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
	elements = len(arrA) + len(arrB)
	merged_arr = []

	a_index = 0
	b_index = 0
	
	for i in range(0, elements):
		print('merged_arr =', merged_arr)
		print('i =', i)
		print('a_index =', a_index)
		print('b_index =', b_index)

		# OOB check A
		if a_index == len(arrA):
			# arrA is depleted, append all contents of arrB to merged_arr
			while b_index != len(arrB):
				merged_arr.append(arrB[b_index])
				b_index += 1
			return merged_arr

		# OOB check B
		if b_index == len(arrB):
			while a_index != len(arrA):
				merged_arr.append(arrA[a_index])
				a_index += 1
			return merged_arr

		# A <= B
		if arrA[a_index] <= arrB[b_index]:
			merged_arr.append(arrA[a_index])
			a_index += 1

		# A > B 
		else:
			merged_arr.append(arrB[b_index])
			b_index += 1

	return merged_arr

"""
def merge_sort(arr):
	#m =

    return arr

# STRETCH: implement the recursive logic for merge sort in a way that doesn't 
# utilize any extra memory
# In other words, your implementation should not allocate any additional lists 
# or data structures; it can only re-use the memory it was given as input
def merge_in_place(arr, start, mid, end):
    # Your code here


def merge_sort_in_place(arr, l, r):
    # Your code here
"""

if __name__ == "__main__":
	arr1 = [3, 6, 9]
	arr2 = [6, 2000, 4000]
	print('arr1 = ', arr1)
	print('arr2 = ', arr2)
	arr3 = merge(arr1, arr2)
	print('arr3 = ', arr3)

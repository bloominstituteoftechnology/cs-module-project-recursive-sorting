def merge(arrA, arrB):
	elements = len(arrA) + len(arrB)
	merged_arr = []

	a_index = 0
	b_index = 0
	
	for i in range(0, elements):

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

def merge_sort(arr):
	m = int(len(arr)/2) 		# Calculate middle
	left = arr[:m]
	right = arr[m:]
	
	if len(left) > 2:			# Recursive merge_sort() on left side until its been completely sorted
		left = merge_sort(left)

	if len(right) > 2:			# Recursive merge_sort() on right side until its been completely sorted
		right = merge_sort(right)

	if len(left) == 2:			# Sort 2-member array (left)  # This could probably be shorter code with a for loop of 2 iterations but this is more readable
		if left[0] > left[1]:
			left[0], left[1] = left[1], left[0]

	if len(right) == 2:			# Sort 2-member array (right)
		if right[0] > right[1]:
			right[0], right[1] = right[1], right[0]
	
	arr = merge(left, right)	# Merge sorted (left) & (sorted) right
	return arr

# STRETCH: implement the recursive logic for merge sort in a way that doesn't 
# utilize any extra memory
# In other words, your implementation should not allocate any additional lists 
# or data structures; it can only re-use the memory it was given as input
#def merge_in_place(arr, start, mid, end):
    # Your code here

#def merge_sort_in_place(arr, l, r):
    # Your code here

# as my input size increases, how much *more* space do we take up?
## not counting the original memory taken up
## aka, as the function runs, does it put more stuff into memory?


arr = [1, 2, 3, 4, 5]

second_arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def counter(arr):
    total = 0

    for thing in arr:
        total += 1

    return total

# Time complexity
## Linear
## Double input, double the steps we took
## O(n)

# Space complexity
## Double input, no extra space
## Constant
## O(1)

def duplicate(arr):
    copy_arr = []

    for thing in arr:
        copy_arr.append(thing)

    return None

# Time complexity
# 1 + len(n)
# O(n)

# Space complexity
# Linear! O(n)

def times_table(n):
    times_table = []

    for i in range(n):
        row = []

        for j in range(n):
            row.append(i * j)

        times_table.append(row)

    return times_table

# print(times_table(5))
table = times_table(5) # 5x5 matrix = 25 
table = times_table(10) # 10x10 matrix = 100
for row in table:
    print(row)

# time complexity
# space complexity
# Both O(n^2)

# Often time and space complexity are the same
# often we trade space for time

# space == memory

# Pandas, Python library
matrix =        [[1, 2, 3, 4, 5],
                 [6, 7, 8, 9, 10],
                 [11, 12, 13, 14, 15]]

first_row = matrix[0]
one = first_row[0]
# Print out all of the numbers in the following array that are divisible by 3:
items = [85, 46, 27, 81, 94, 9, 27, 38, 43, 99, 37, 63, 31, 42, 14]
# The expected output for the above input is:
# 27
# 81
# 9
# 27
# 99
# 63
# 42

[print(item) for item in items if item % 3 == 0]
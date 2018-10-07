"""Given an array of integers, write a function to determine 
whether the array could become non-decreasing by modifying at most 1 element.

For example, given the array [10, 5, 7], you should return true, since we 
can modify the 10 into a 1 to make the array non-decreasing.

Given the array [10, 5, 1], you should return false, since 
we can't modify any one element to get a non-decreasing array."""

array = [10, 5, 7]

result = 0

for x in range(len(array)):

	if not x==(len(array) -1) and array[x] > array[x+1]:
		result +=1

if result <=1:
	print(True)
else:
	print(False)

"""This problem was asked by Facebook.

Given a multiset of integers, return whether it can be partitioned into 
two subsets whose sums are the same.

For example, given the multiset {15, 5, 20, 10, 35, 15, 10}, it would return true, 
since we can split it up into {15, 5, 10, 15, 10} and {20, 35}, which both add up to 55.

Given the multiset {15, 5, 20, 10, 35}, it would return false, since we can't 
split it up into two subsets that add up to the same sum."""

def doesMain():
    """
    Calculate the sum of the data.

    Args:
    """
	data = [15,5,20,10,35,15,10]
	data.sort()
	total = sum(data)
	if total / 2 == total //2 :
		return contain(array,total / 2 , 0)
	else:
		return False

def contain(array , number , index):
    """
    Return true if the array is contained in the array.

    Args:
        array: (array): write your description
        number: (int): write your description
        index: (int): write your description
    """
	if index == len(array):
		return True
	if array[index] == number:
		return True
	elif array[index] < number:
		return contain(array, number -1, index+1)
	else :
		return contain(array, number, index+1)

def sum(array):
    """
    Return the sum of all elements.

    Args:
        array: (array): write your description
    """
	result = 0
	for i in array:
		result += i
	return result

	print()
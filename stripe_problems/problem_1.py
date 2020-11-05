"""This problem was asked by Stripe.

Given an array of integers, find the first missing positive integer in linear time and constant
space. In other words, find the lowest positive integer that does not exist in the array.

The array can contain duplicates and negative numbers as well.

For example, the input [3, 4, -1, 1] should give 2. The input [1, 2, 0] should give 3.

You can modify the input array in-place."""


# function to the main problem
def find_missing_value(array):
    """
    Finds the missing missing value.

    Args:
        array: (array): write your description
    """
    # sorting the array
    array.sort()

    # if the array is empty we return 1 since 1 is the first positive number.
    if len(array) == 0:
        return 1

    # otherwise we search.
    else:

        # take the first of the array.
        k = array[0]
        # if k is bigger than two then we should return 1 since the array is sorted.
        if k >= 2:
            return 1
        # otherwise we search for it
        for i in range(len(array)):
            # if k is not like the current element than this k is missing number.
            if k != array[i]:
                return k

            # if not the case we increment k.
            k += 1

            # if we increment and k is 0 we re-increment it.
            if k == 0:
                k += 1
        # finally return k if the number was out the range of the array.
        # like [1,2,3] here the missing is 4.
        return k


# testing the code
print(find_missing_value([3, 4, -1, 1]))
print(find_missing_value([1, 2, 0]))
print(find_missing_value([1, 2, 3, 4, 6]))
print(find_missing_value([]))

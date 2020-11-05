"""This problem was asked by Google.

Given an array of integers and a number k, where 1 <= k <= length of the array,
compute the maximum values of each subarray of length k.

For example, given array = [10, 5, 2, 7, 8, 7] and k = 3,
we should get: [10, 7, 8, 8], since:

10 = max(10, 5, 2)
7 = max(5, 2, 7)
8 = max(2, 7, 8)
8 = max(7, 8, 7)
Do this in O(n) time and O(k) space. You can modify the input
array in-place and you do not need to store the results.
You can simply print them out as you compute them."""


# the solution functions.
def max_value(arr, k):
    """
    Returns the maximum value of arr.

    Args:
        arr: (array): write your description
        k: (todo): write your description
    """
    start = 0
    end = k
    while end <= len(arr):
        print(max(arr[start:end]))
        end += 1
        start += 1


# testing the solution.
max_value([10, 5, 2, 7, 8, 7], 3)

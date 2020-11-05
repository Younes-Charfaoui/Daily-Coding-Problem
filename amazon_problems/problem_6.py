"""This problem was asked by Amazon.

Given an array of numbers, find the maximum sum of
any contiguous subarray of the array.

For example, given the array [34, -50, 42, 14, -5, 86], the maximum sum would be 
137, since we would take elements 42, 14, -5, and 86.

Given the array [-5, -1, -8, -9], the maximum sum would be 0, since we would 
not take any elements.

Do this in O(N) time.
"""


def solve(arr):
    """
    Solve arr.

    Args:
        arr: (array): write your description
    """
    mx = 0
    sum = 0
    for a in arr:
        sum += a
        if sum < 0: sum = 0
        mx = max(mx, sum)
    return mx

print(solve([34, -50, 42, 14, -5, 86])) # returns 137
print(solve([-5, -1, -8, -9])) # returns 0
